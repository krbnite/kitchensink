---
title: Multi-GPU Training with TensorFlow Estimators
layout: post
tags: tensorflow keras multi-gpu deep-learning
---

# Multi-GPU Training with TensorFlow Estimators
Your Keras model works great, so why bother learning about TF Estimators?  Well,
let's say our next task is to train that same model architecture, but on a 
dataset that is several TBs in size.  We might want to use a better EC2 
instance -- one that has several GPUs.  Let's say training would take around
8 days on a single GPU, but that we estimate it will take only 1 day on this
multi-GPU machine:  will your model automatically take advantage of all
available GPUs?  Probably not.  But if you wrap it in a TF Estimator, it
will.

```
from tensorflow.keras import layers, models, losses
from tensorflow.keras.datasets import mnist
import tensorflow as tf
import tensorflow_datasets as tfds

# Design and Compile Model Architecture
model = models.Sequential([
    layers.Input((28,28,1)),
    layers.BatchNormalization(),
    layers.Conv2D(filters=64, kernel_size=3, strides=2),
    layers.BatchNormalization(),
    layers.ReLU(),
    layers.Dropout(0.5),
    layers.Flatten(),
    layers.Dense(32),
    layers.PReLU(),
    layers.Dense(10),
    layers.Softmax(),
])
model.compile(
    optimizer='adam', 
    loss=losses.SparseCategoricalCrossentropy(), 
    metrics=['accuracy'], 
)

# Convert Keras model to TF Estimator
est_model = tf.keras.estimator.model_to_estimator(keras_model = model)

# Some standard image pre-processing code 
def preprocess(image, label):
  image = tf.cast(image, tf.float32)
  image = (image/127.5) - 1
  return image, label
# For some reason, you need to load tfds data inside input function, or
#   you get runtime errors 
def shuffle_and_batch(batch_size, mode='train'):
  mode = {'tr':'train','te':'test'}[mode.lower()[:2]]
  data = tfds.load('mnist', as_supervised=True)[mode]
  shuffle_data = data.map(preprocess).shuffle(500).batch(batch_size)
  return shuffle_data

# Train  (EquivNumEpochs = batch_size * steps / total_num_samples)
est_model.train(input_fn=lambda: shuffle_and_batch(32, 'train'), steps=500)

# Test
est_model.evaluate(input_fn=lambda: shuffle_and_batch(32, 'test'), steps=10)
```

In this example, I set `steps=500`, which means it doesn't even go through the
entire training set once.  However, I still got about 97% accuracy on the test
set.  Crazy.  If you do not specify steps, it will go through the entire 
training set once (from what I understand).  So if you want many epochs, then
you have to do the math... There might be a workaround where you can specify
epochs instead of steps somewhere...but it's not super obvious.

* https://stackoverflow.com/questions/56612386/defining-the-input-function-for-tensorflow-pre-made-estimator/56615591
* https://www.tensorflow.org/api_docs/python/tf/data/Dataset

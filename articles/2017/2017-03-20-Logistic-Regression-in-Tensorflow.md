---
title: Logistic Regression in Tensorflow
layout: post
tags: deep-learning machine-learning tensorflow python wwe
---

This is a short follow-up to [Linear Regression in Tensorflow](2017-03-20-Linear-Regression-in-Tensorflow.md).
The point is simple: logistic regression can be written in almost the same
neural-network shape as linear regression, but the model output is interpreted
as a probability.

In the linear-regression example, the model produced a raw continuous value:

```python
y_pred = tf.add(tf.matmul(x_input, w), b)
```

For logistic regression, that raw value is usually called a logit. Passing the
logit through the logistic function, or sigmoid function, turns it into a value
between 0 and 1:

```python
logits = tf.add(tf.matmul(x_input, w), b)
y_prob = tf.nn.sigmoid(logits)
```

That is the intuitive bridge from linear regression to binary classification.
Keep the linear weighted sum, then wrap it in a probability-producing function.

## Minimal TensorFlow 1 Example

This keeps the 2017 TensorFlow 1 style of the original note while making the
classification target explicitly binary.

```python
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# Generate a one-feature binary classification problem.
np.random.seed(42)
x_data = np.random.rand(10000, 1).astype(np.float32)
true_logits = 8.0 * x_data - 4.0
y_probs = sigmoid(true_logits)
y_data = (np.random.rand(10000, 1) < y_probs).astype(np.float32)

x_train, x_vt, y_train, y_vt = train_test_split(
    x_data, y_data, test_size=0.5, random_state=42
)
x_val, x_test, y_val, y_test = train_test_split(
    x_vt, y_vt, test_size=0.5, random_state=31
)

x_input = tf.placeholder(shape=(None, 1), dtype=tf.float32)
y_input = tf.placeholder(shape=(None, 1), dtype=tf.float32)

w = tf.Variable(
    tf.truncated_normal((1, 1), mean=0.0, stddev=np.sqrt(2.0), dtype=tf.float32),
    name="weight",
)
b = tf.Variable(tf.zeros(1, dtype=tf.float32), name="bias")

logits = tf.add(tf.matmul(x_input, w), b)
y_prob = tf.nn.sigmoid(logits)

loss = tf.reduce_mean(
    tf.nn.sigmoid_cross_entropy_with_logits(labels=y_input, logits=logits)
)
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

predicted_class = tf.cast(y_prob >= 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted_class, y_input), tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(100):
        sess.run(train, feed_dict={x_input: x_train, y_input: y_train})

        if epoch % 25 == 0:
            train_loss = sess.run(loss, feed_dict={x_input: x_train, y_input: y_train})
            val_acc = sess.run(accuracy, feed_dict={x_input: x_val, y_input: y_val})
            print(epoch, train_loss, val_acc)
```

The workflow is nearly the same as the linear-regression version:

1. Declare placeholders for inputs and labels.
2. Initialize weights and bias.
3. Build a linear expression for the logits.
4. Convert logits to probabilities with sigmoid.
5. Train with a classification-appropriate loss.

The key distinction is the loss function. Squared error can be used in toy
examples, but cross-entropy is the natural objective for this binary
classification setup.

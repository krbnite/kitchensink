NOTE FROM 2026: This notebook was a part of an old directory of mine with tons of old code, throwaway notebooks,
notes, and odds and ends. Most of it was garbage, but this looked worth preserving in my kitchensink repo. This
file was made 6 years ago, so around 2020. 

------

TF2.2


Old way.  

Some older things require you to do:
```python
import tensorflow.compat.v1 as tf
```

Other times, just this will suffice:
```
tf.compat.v1.disable_eager_execution() 
```

And then there are occasions where your code needs both!  Ultimately,
it's best to switch to TF2.2 syntax...  Here are some examples of
computing gradients in various ways.


# TF1 Compatibility Mode
Basic Setup
```python
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()  

# Get Data
(x_trn,y_trn),(x_tst,y_tst) = get_data()
x_gradtest1 = x_trn[:1]
x_gradtest2 = x_trn[:10]

# Get Model
model = get_model()
```


## Gradients w.r.t. `model.output` 

### Gradients at each Layer Output

This way gets you gradients (w.r.t. model.output) at output of each trainable layer.

Note that model does not have to be trained to do any of this: once it's compiled,
go ahead and go wild!  Also, if you manually train on batches instead of using 
`model.fit`, you can keep track of things like weights, gradients, and outputs
with any level of granularity and control that you like.  Alternatively, you can
have similar control by using a Keras Callback (likely a LambdaCallback or a 
Custom Callback).  

```python
# Extract Trainable Layers
trainable_layers = [
    layer for layer in model.layers if len(layer.trainable_weights) > 0
]

# Extract the output at each trainable layer
trainable_layer_output_tensors = [
    layer.output for layer in trainable_layers
]

# Compute the gradient of the output at each trainable layer
#     w.r.t. `model.output`
grad_tensors = tf.keras.backend.gradients(
    model.output, trainable_layer_output_tensors
)  

# Build a camera to install inside the neural net at the output
#    of each trainable layer on the forward pass, and at its 
#    gradient on the backward pass
layer_cam = tf.keras.backend.function(
    [model.input], [output_tensors, grad_tensors]
)  

#======================================================================
# Take a Snapshot!
#======================================================================
#   - NOTE: for each trainable output layer, both `output_values`
#     and `grad_values` return a list of lists of lists   
#     * the top-level list has elements corresponding to each trainable   
#       layer; 
#     * for each trainable layer, there is a sublist corresponding to each 
#       data point in the `layer_cam` input;
#     * for each data point, there is a sublist of layer outputs (or 
#       gradients)
#   - POINT: the next couple of print statements could be overwhelming
#     if you `layer_cam` input has too many data points; might be good
#     to summarize (e.g., compute a histogram: 
#                    `np.histogram(grad_values[0][0])`)
output_values, grad_values = layer_cam([x_gradtest1])


# All Outputs (1 Data Point)
print(f'{"="*80}\nAll Outputs\n{"="*80}\n')
[print(f'{layer.name:10}\n{"-"*80}\n', out.squeeze(), end='\n'*3) 
    for layer,out in zip(trainable_layer_output_tensors, output_values)
]; 

# All Gradients (1 Data Point)
print(f'{"="*80}\nAll Gradients\n{"="*80}\n')
[print(f'{layer.name:10}\n{"-"*80}\n', np.round(grad,3).squeeze(), end='\n'*3) 
    for layer,grad in zip(trainable_layer_output_tensors, grad_values)]; 
    

#======================================================================
# Take a BIGGER snapshot (for histogram)
#======================================================================
output_values, grad_values = layer_cam([x_tst])

#  Histograms (all of x_tst)
print(f'{"="*80}\nHistograms\n{"="*80}\n')
out_hist = list()
grad_hist = list()
for layer,out,grad in zip(trainable_layer_output_tensors, output_values, grad_values):
    name = trainable_layer.name
    ohist = np.histogram(out)
    ghist = np.histogram(grad)
    out_hist.append({'name': name, 'hist': ohist})
    grad_hist.append({'name': name, 'hist': ghist})
    print(f'{name:10}\n{"="*80}\n\n', 
        f'{"Outputs":10}\n{"-"*80}\n', ghist, '\n\n' 
        f'{"Gradients":10}\n{"-"*80}\n', ohist, 
        end='\n'*3)
```


### Gradients at each Trainable Weight (w.r.t. to model output)

Alternatively, compute gradients (w.r.t. model.ouptput) for all trainable weights

```python
# Extract Trainable Weights
trainable_weights = model.trainable_weights

# Compute the gradient of the output at each trainable layer
#     w.r.t. `model.output`
grad_tensors = tf.keras.backend.gradients(
    model.output, trainable_weights
)

# Build a camera to install inside the neural net at the output
#    of each trainable weight on the forward pass, and at its 
#    gradient on the backward pass
layer_cam = tf.keras.backend.function(
    [model.input], [trainable_weights, grad_tensors]
)

#======================================================================
# Take a small snapshot (1 data point)
#======================================================================
weight_values, grad_values = layer_cam([x_gradtest1])

# All Weights (1 Data Point)
print(f'{"="*80}\nAll Weights\n{"="*80}\n')
[print(f'{weight.name:10}\n{"-"*80}\n',value.squeeze() end='\n'*3) 
    for weight,value in zip(trainable_weights, weights)
]; 

# All Gradients (1 Data Point)
print(f'{"="*80}\nAll Gradients\n{"="*80}\n')
[print(f'{layer.name:10}\n{"-"*80}\n',np.round(grad,3).squeeze(), end='\n'*3) 
    for layer,grad in zip(trainable_weights, grads)
]; 


#======================================================================
# Take a BIGGER snapshot (for histogram)
#======================================================================
weight_values, grad_values = layer_cam([x_tst])

#  Histograms (all of x_tst)
print(f'{"="*80}\nHistograms\n{"="*80}\n')
weight_hist = list()
grad_hist = list()
for layer,weight,grad in zip(trainable_weights, weight_values, grad_values):
    name = trainable_layer.name
    weight_hist.append({'name': name, 'hist': np.histogram(weight)})
    grad_hist.append({'name': name, 'hist': np.histogram(grad)})
    print(f'{name:10}\n{"="*80}\n\n', 
        f'{"Weights":10}\n{"-"*80}\n', weight_hist[-1]['hist'], '\n\n' 
        f'{"Gradients":10}\n{"-"*80}\n', grad_hist[-1]['hist'], 
        end='\n'*3)

```

-------------------------------------------------------------------------


## Gradients w.r.t. the Loss Function

Basic set up...

Here, instead of importing `tensorflow.compat.v1 as tf`, I try to do 
the bare minimum "TF1"-ness.  Turns out though that I still need to disable
eager execution...

```python
import numpy as np
import tensorflow as tf
tfv = float('.'.join(tf.__version__.split('.')[:2]))
if tfv < 2:
    from tensorflow import InteractiveSession, global_variables_initializer
else:
    tf.compat.v1.disable_eager_execution()
    from tensorflow.compat.v1 import InteractiveSession, global_variables_initializer

model = tf.keras.models.Sequential([
    tf.keras.layers.Input((28,28), dtype=tf.float32),
    tf.keras.layers.Reshape((28,28,1)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(filters=10, kernel_size=3, strides=2),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=10),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(units=10)
])
model.compile(
    optimizer='sgd', 
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True,name='loss'),
)
(x_trn,y_trn),(x_tst,y_tst) = tf.keras.datasets.mnist.load_data()
x_trn, y_trn = x_trn.astype(np.float32), y_trn.astype(np.float32)
x_tst, y_tst = x_tst.astype(np.float32), y_tst.astype(np.float32)
x_gradtest1 = x_trn[:1]
x_gradtest2 = x_trn[:10]
#history = model.fit(x_trn, y_trn, epochs=1)
```

Ok...

## Gradients of Trainable Weights w.r.t. Loss Function
Above, I was computing gradients w.r.t. `model.output`, which could come in handy
somehow, some way...but it's not what is typically computed.  

What's typically computed is the gradient of the Loss Function.



Wait... This way keeps crashing now...

```python
# Gradients
trainable_weights = model.trainable_weights
loss_tensor = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss = loss_tensor(model.output, y_tst)
gradients = tf.keras.backend.gradients(loss, trainable_weights)


sess = InteractiveSession()
sess.run(global_variables_initializer())

evaluated_gradients = sess.run(
    gradients, 
    feed_dict = {model.input: x_gradtest1}
)
```







-----------------------------------------------------------------

For any future readers that this might help, I've included supplemental code below (e.g., a `get_model` function that can be used in the above code examples).

```python
#-----------------------------------------------------------
def get_data(
    tinker_with = 'mnist',
):
    assert tinker_with in ['mnist','cifar10','cifar100'],\
        "Unrecognized dataset: choose from 'mnist' (default), "+\
        "'cifar10', or 'cifar100'"
    if tinker_with == 'mnist':
        dataset = tf.keras.datasets.mnist.load_data()
    elif tinker_with == 'cifar10':
        dataset = tf.keras.datasets.cifar10.load_data()
    else:
        dataset = tf.keras.datasets.cifar100.load_data()
    return dataset

#-----------------------------------------------------------
def get_model(channel_depth=1):
    if isinstance(channel_depth,str): 
        channel_depth = channel_depth.lower()
    assert channel_depth in [1,3,'mnist','cifar10','cifar100'],\
        "Unacceptable channel_depth: choose from 1, (default), "+\
        "3, 'mnist', 'cifar10', or 'cifar100'"
    C = 1 if channel_depth in [1,'mnist'] else 3
    #----------------  Build Model  -------------------
    vis     = tf.keras.layers.Input((28,28))
    reshape = tf.keras.layers.Reshape((28,28,C))(vis)
    norm_l0 = tf.keras.layers.BatchNormalization()(reshape)
    drop_l0 = tf.keras.layers.Dropout(0.1)(norm_l0)
    conv_l1 = tf.keras.layers.Conv2D(filters=8, kernel_size=3, 
                  padding='same', use_bias=False)(drop_l0)
    norm_l1 = tf.keras.layers.BatchNormalization()(conv_l1)
    relu_l1 = tf.keras.layers.ReLU()(norm_l1)
    pool_l1 = tf.keras.layers.MaxPool2D(pool_size=2, strides=2,
                  padding='same')(relu_l1)
    conv_l2 = tf.keras.layers.Conv2D(filters=4, kernel_size=3, 
                  strides=2, padding='same', use_bias=False)(pool_l1)
    norm_l2 = tf.keras.layers.BatchNormalization()(conv_l2)
    relu_l2 = tf.keras.layers.ReLU()(norm_l2)
    pool_l2 = tf.keras.layers.MaxPool2D(pool_size=2, strides=2,
                  padding='same')(relu_l2)
    flat_l3 = tf.keras.layers.Flatten()(pool_l2)
    dens_l3 = tf.keras.layers.Dense(10)(flat_l3)
    relu_l3 = tf.keras.layers.ReLU()(dens_l3)
    drop_l3 = tf.keras.layers.Dropout(0.2)(relu_l3)
    dens_l4 = tf.keras.layers.Dense(10)(drop_l3)
    output  = tf.keras.layers.Softmax()(dens_l4)
    #---------------  Compile Model  ------------------
    model = tf.keras.models.Model(vis, output)
    model.compile(optimizer=tf.keras.optimizers.Adam(), 
        loss=tf.keras.losses.SparseCategoricalCrossentropy(), 
        metrics=['accuracy']) 
    return model

#-----------------------------------------------------------
from sklearn.model_selection import train_test_split
def train(
    model,
    x_train, y_train, 
    batch_size=32, 
    epochs=100, 
    validation_split=0.2, 
    shuffle = True, 
    early_stopping = True,
    es_monitor = 'val_loss',
    es_min_delta = 0,
    es_patience = 7,
    es_verbose = 0,
    es_mode = 'auto',
    es_baseline = None,
    es_restore_best_weights = True,
    tensorboard = True,
    tb_log_dir = './logs', 
    tb_histogram_freq = 5, 
    tb_update_freq = "epoch",
):
    callbacks = list()
    if early_stopping:
        early_stopping = tf.keras.callbacks.EarlyStopping( 
            monitor   = es_monitor, 
            min_delta = es_min_delta, 
            patience  = es_patience, 
            verbose   = es_verbose, 
            mode      = es_mode, 
            baseline  = None, 
            restore_best_weights = es_restore_best_weights,
        )
        callbacks.append(early_stopping)
    if tensorboard:
        tensorboard = tf.keras.callbacks.TensorBoard( 
            log_dir = tb_log_dir, 
            histogram_freq = tb_histogram_freq, 
            update_freq = tb_update_freq,
        ) 
        callbacks.append(tensorboard)
    """
    NOTE: Though Keras' model.fit method can directly 
      accept the `validation_split` parameter, it is
      designed to take the associated validation data 
      from the end of the training set pre-shuffle. 
      This policy is not ideal for datasets that come 
      stock with some order and structure (e.g., there 
      is a risk of having unseen classes in the 
      validation set).  To hedge against this risk,
      we will instead pass the `validation_split`
      parameter to sklearn's `train_test_split`,
      then pass the split-off validation data to the 
      `validation_data` parameter in model.fit. 
    """
    x_train, x_val, y_train, y_val = train_test_split(
        x_train, y_train, 
        test_size = validation_split, 
        shuffle   = True,
        stratify  = y_train,
    )
    history = model.fit( 
        x_train, y_train, 
        batch_size      = batch_size, 
        epochs          = epochs, 
        validation_data = (x_val, y_val), 
        shuffle         = shuffle, 
        callbacks       = callbacks,
    )
    return history

#-------------------------------------------------------------
def get_simple_FC_model(
    input_shape,
    layers, 
    activation, 
    initializer,
    optimizer = 'sgd',
):
    
        
    model = tf.keras.models.Sequential()
    
    # Add Input Layer with input_dim parameter
    if isinstance(input_shape,(int,float)):
        input_shape = (int(input_shape),)
    model.add(
        tf.keras.layers.Input(shape = input_shape, name='input')
    )
    
    # Add hidden layers
    if isinstance(layers, (int,float)):
        layers = [int(layers)]        
    model.add(
        tf.keras.layers.Dense(
            units = layers[0], 
            kernel_initializer = initializer, 
            name = 'hidden_1',
        )
    )
    model.add(
        tf.keras.layers.Activation(activation, name='activation_1')
    ) 
    for idx,layer in enumerate(layers[1:]):
        model.add(
            tf.keras.layers.Dense(
                units = layer, 
                kernel_initializer = initializer, 
                name = f'hidden_{idx+2}',
            )
        )
        model.add(
            tf.keras.layers.Activation(activation, name=f'activation_{idx+2}')
        ) 
    # Add output layer
    model.add(
        tf.keras.layers.Dense(
            units=1, 
            activation='sigmoid', 
            kernel_initializer=initializer, 
            name='output',
        )
    )   
    # Compiles the model
    model.compile(
        loss      = 'binary_crossentropy', 
        optimizer = optimizer, 
        metrics   = ['acc'],
    )   
    return model

```


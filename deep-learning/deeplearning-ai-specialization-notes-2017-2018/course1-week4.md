

## What is a deep neural network?

We saw that logistic regression can be represented as a single-layer (shallow) neural network:
<img src=./images/1-layer-nn.png>

And we saw that we could add an additional layer (called a hidden layer) to generalize logistic regression to a 2-layer neural network:
<img src=./images/2-layer-nn.png>

Well, what's stopping us from adding another hidden layer?
<img src=./images/3-layer-nn.png>

Or another several hidden layers?
<img src=./images/6-layer-nn.png>

This last network is a 6-layer network, aka a network w/ 5 hidden layers.  That's pretty deep, right?  Certainly not shallow like the
neural network represenation of logistic regression.

## Some more notational agreements
* L will denote the number of layers that make a NN
* n^[l] := number of nodes in layer l (i.e., number of components in the lth "Layer Vector")
* 0th layer is input layer
* Lth layer is output layer
* Number of nodes in input layer denoted as n^[0] or n_x
* a^[l] = gl(z^[l]) = gl(w^[l]a^[l-1]+b^[l])
  - a^[0] = x
  - a^[L] = y_pred


## Forward Prop in a DNN
* z^[1] = w^[1]a^[0] + b^[1], where a^[0]=x
* a^[1] = g1(z^[1])
* z^[2] = w^[2]a^[1] + b^[2]
* a^[2] = g2(z^[2])
* ...
* z^[L] = w^[L]a^[L-1] + b^[L]
* y_pred = gL(z^[L])

This can be done a single data point at a time, or in a vectorized fashion.  The algebraic
equations look exactly the same (though Ng denotes the vectorized quantities w/ capital letters:
* Z^[l] = W^[l]A^[l-1] + b^[l-1]
* b is not capitalized to denote that it is broadcasted

Note that everything can be vectorized/parallelized except the stepwise fashion that layers are computed.


## Getting Your Matrix Dimensions Right
Say we have a 5-layer neural network, NN = {2; 3, 5, 4, 2, 1}, where the numeric sequence represents the size 
of each layer in sequence (the 0th/input layer is listed w/ a semicolon since it is not considered part of the layer count).

### What are the dimensions of the Z's, B's, and A's given m training samples?
* Remember: Ng uses columnar records such that a layer's features form a column vector
* So for 1 data point, we have z1.shape = (3,1)  
* For m data points, we have Z1.shape = (3,m)
* Similarly, for m data points, the second layer has Z2.shape = (5,m)
* ...and so on!
* **So the layer vectors have the following form in Ng notation: (n^[l], m)**
* NOTE: technically, you do not need to make (n^[l], m) bias matrices since NumPy will broadcast the (n^[l],1) bias vector 
* Note that in TensorFlow, the shapes are the transpose of Ng shapes
  - Z1_TF.shape = (m,3)
  - Z2_TF.shape = (m,5)

### What are the shapes of the weight matrices connecting layers?
* Our layers are column vectors and we are pre-multiplying the layer vectors, np.dot(W,x)
* This means that W1 needs as many columns as X has rows/features: W1.shape[1] = 2
* It also means that W needs as many rows as the next layer has nodes: W1.shape[0] = 3
* **So the weight matrices have the following form in Ng notation: (n^[l], n^[l-1])**
  - (3,2)
  - (5,3)
  - (4,5)
  - (2,4)
  - (1,2)
* Note that in TensorFlow, that the shapes are the transpose of Ng shapes
  - W1_TF.shape = (2,3)
  - W2_TF.shape = (3,5)
  - I like this notation b/c it reads straight across as "W1 connect 2 nodes to 3 nodes, W2 connect 3 nodes to 5 nodes, etc"

### What are the sapes of the gradients?
* A derivative of a tensor function always has the same shape as the tensor function itself.
* e.g., dZ1.shape == Z1.shape


## Why Deep Representations?
Technically if a 2-layer NN is wide enough, it can well-approximate nearly any function... Yet in practice, with limited data,
limited RAM, and limited time, this doesn't really work out so well.  I've read that though there is a theorem that suggests
a wide enough hidden layer can do the job, there is no actual way to compute how wide a layer has to be for a particular
(input, output) map to be approximated.

Turns out that adding additional hidden layers does a similar job, but does not seem to require nearly as many nodes.
That is, oftentimes two relatively narrow hidden layers perform better than a single, wide layer.

When exploring how each successive layer works, a simple-to-complex heirarchy of detail is found.  For example, in an image t
he first layer detects very simple
patterns (e.g., lines, curves).  The second layer composes those patterns to form more complex patterns (e.g., squares, circles, etc).
A third layer is able to extract even more complex features by composing those from the second layer (e.g., face-like shapes).  

<img src=./images/deep-heirarchy.png>

Audio is another example: the first layer might identify simple wave forms, like constant pitches, rising and falling tones.  The 
second layer might compose those to generate familiar monosyllabic sounds.  A third layer might begin to have extracted complex words.
Etc.

This heirarchical representation of data is thought to be similar to how the human mind operates...

### Circuit Theory
Another reason that deep neural networks are effective is backed up by circuit theory.  
Informally the theorem says that there exist functions that can be well-approximated
by a "small" L-layer network of logitc gates (e.g., AND, OR, and NOT gates) that 
shallower networks require exponentially more hidden units to do the same job.


Ng gives an example of computing the parity of a group of bits by creating a deep network of XOR gates.
The number of nodes needed for the deep network is relatively few when compared to the number of nodes
required if one demands the network have only one hidden layer.

<img src=./images/deep-vs-shallow-xor.png>


### Branding
"Deep" just sounds cool, so everyone loves it :-p

You can always start with logistic regression and go from there.

-------------------------------------------

## Building Blocks of a DNN
Notice in forward propagation, at layer l, the input is the previous activation, a^[l-1]:
* z^[l] = w^[l]a^[l-1] + b^[l]

Likewise, the output of the lth layer is its activation:
* a^[l] = gl(z^[l])

However, in addition to a layer's activation output for input into the next layer in forward propagation, 
the lth linear transformation, z^[l], is important to keep around for the backprop.  In last week's 
project, we stored these variables in a cache.

For backward propagation, notice that the input at a given step is da^[l] (and the cached z^[l]) and the output is da^[l-1] (and dw^[l] and db^[l]).

<img src=./images/fwd-and-bwd-fcns.png>

<img src=./images/full-pass.png>
Ng says he keeps w^[l] and b^[l] in the cache at each step as well b/c it simplifies things from an implementation standpoint...

The full pass, of course, ends with updating the weights:
* w^[l] <-- w^[l] - learnrate\*dw^[l]
* b^[l] <-- b^[l] - learnrate\*db^[l]

--------------------------------------------------

## Backward Prop for Layer l
### One data point at a time
* Input da^[l]
* Output da^[l-1], dW^[l], db^[l]
* dz^[l] = da^[l]\*gl'(z^[l])
* dW^[l] = \<dz^[l], a^[l-1]\>
* db^[l] = dz^[l]
* da^[l-1] = \<(W^[l])^T, dz^[l]\>

### Vectorized
* Input dA^[l]
* Output dA^[l-1], dW^[l], db^[l]
  - dW^[l] is same on 1 or m data points
  - db^[l] is broadcasted for m data points
* dZ^[l] = dA^[l]\*gl'(Z^[l])
* dW^[l] = (1/m)\<dZ^[l], (A^[l-1])^T\> / m
* db^[l] = np.sum(dZ^[l], axis=1, keepdims=1) / m
* dA^[l-1] = \<(W^[l])^T, dZ^[l]\>

## Initializing the Input for Fwd and Bwd Passes
Obviously the forward pass starts by inputting a^[0], which is x the input data to the network.
But what about the backward pass?

The backward pass begins with input da^[L].  The the binary classification cost fcn we have been using:
* da^[L] := dL/da^[l] = -(y/a) + (1-y)/(1-a)

## Where does the power come from?
Sometimes it might be surprising how well a neural network can perform after training.  
Given such a simple algorithm, one might wonder where this power comes from.  Ng emphasizes that
the power comes from the data.  The algorithm itself can be quite weak without enough data.

## Parameters vs Hyperparameters
The parameters of a NN are the weights and biases.  These parameters are tuned via the training process.
However, one will notice that other tunable quantities exist, e.g., the learning rate, number of epochs,
batch size, number of hidden layers, number of units at each layer, and the activation function at each layer. 
These parameters are called hyperparameters: they not tuned during training, 
but instead they are chosen prior to training.  One can choose multiple instances of each hyperparameter,
but each unique set of chosen hyperparameters must undergo its own training session.

Additional hyperparameters might include ones associated with momentum and regularization.

Applied deep learning is a very empirical process -- trial and error, iterate and improve. 
In the next course, we will develop systematic ways of converging on the best hyperparameters
for any given project.









  

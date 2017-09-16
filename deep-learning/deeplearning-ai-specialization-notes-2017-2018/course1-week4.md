

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


  



##Typical 2-Layer NN Representation
Oftentimes, a NN is represented as follows:
![](./images/typical-nn-representation.png)
In this representation, each node represents both the linear transformation and subsequent activation.
The edges represent matrix weights.

Note that "nodes" are just the components of a vector.

Also note that this is called "2 layer" b/c the input layer is not counted in this nomenclature.

## Notational Representation
How should we identify which layer a matrix weight or node is referring to?
Ng uses a square-bracketed superscript, like so:
![](./images/layer-number-notation.png)
However, in this markdown file, we will just put the layer number after a semi-color, e.g.,
W[i,j;k] is the (i,j)th weight of the matrix flowing into layer k.

If we are not specifying matrix components, the notation in these markdown files will
look like W[;k].  

## Some Terminology
![](./images/some-terminology.png)

Note the following notational representations:

* a[i,j;0] = identity(x[i,j]) = x[i,j]: the activation on the input layer is the identity function, i.e.,
   the "output values" in the input layer are transferred to the first hidden layer unchanged
* z[;1] = <w[;1],x>+b
* a[;1] = activation(z[;1])

A particular "node" in a layer refers to a particular component of the layer vectors, e.g., in a
3-node layer

## Algebratize!
![](./images/algebratize-the-network.png)


z[i,j;L] = w[i,k;L]a[k,j;L-1] + b[i,j;L]   # Einstein summation for pre-semicolon indices
a[i,j;L] = activation(z[i,j;L])

For L=1, x[i,j] = a[k,j;0]

## Choice of Activation Function
Sigmoid activation is a great way to introduce activation functions:
* it's differentiable (as opposed to the step function used in a perceptron)
* it's used in logistic regression
* logistic regression can be set up as a simple neural network

However, it's not really a great activation function to use on a bunch of hidden layers.  
People like it b/c it's theoretically pleasing... But a related activation, tanh, 
usually works much better in practice. Ng says, "I pretty much never use a sigmoid activation
function anymore... tanh is always superior. The one exception is for an output layer."

Action both the "sigmoid fcn" and tanh are considered sigmoid functions.  What we call the
"sigmoid fcn" is also known as the logistic funtion.  

Sigmoid and Tanh can both stall learning... Both saturate on large postive and negative values,
inducing a vanishing gradient --- and so small-to-no updates.  

The solution? The REctified Linear Unit (RELU):  relu(x) = max(0,x)

The fact that RELU is not strictly differentiable does not matter in practice.  However, the 
vanishing gradient still exists for negative values...  For many applications, this doesn't matter.
However, if it does, then a leaky RELU is better:  lrelu = max(alpha*x, x), where alpha is a shrink parameter.

In practice, using a RELU trains a network much faster than sigmoid or tanh activations b/c
it addresses the vanishing gradient enough...

Sigmoid:  Never use except on output layer
Tanh:  If you think you want sigmoid on a hidden layer, use tanh instead
Relu: If you're thinking about using tanh, just F'n use the RELU
Leaky Relu:  This might help. 

## So many choices
That's deep learning.  Deal with it!  If you're not sure, try 'em all.  Start w/ best practices,
but always explore a bit.  Usually the type of problem you are working on is most amenable to a 
certain set of choices.

## The purpose of the nonlinear activation function
To. Add. Nonlinearity.  

That's it!

Without a nonlinear activation, the composition of linear transformation is just a linear transformation.
Thus the nonlinear activations allow the network to learn nonlinear functions!

"A linear hidden layer is more-or-less useless." --Ng

If the last layer is supposed to be a regression, then a linear transformation might be best.  
However, even in the regression case that's not always true: RELU is better for predicting 
house prices b/c it does not allow negative values.










Electricity transformed countless industries: AI will bring about an equally-powerful transformation

## Specialization
* Course 1:  Neural Networks and Deep Learning 
  - Covers fundamentals/foundations
  - Learn to build/train deep NNs
  - Will build a cat classifier
* Course 2: Improving DNNs
  - Hyperparameter tuning
  - Regularization
  - Optimization (Adam, RMSProp, etc)
* Course 3: Structuring your Machine Learning Project
  - best practices
  - dealing w/ differences in data distributions inherent in split data sets
  - end-to-end deep learning: should you use it?
* Course 4:  Convolutional Neural Networks (CNNs)
* Course 5:  NLP / Sequence Models
  - RNN, LSTM, etc
  
# Week 1
## What is a Neural Network?
* DL just refers to building "deep" neural networks

### Housing Price Prediction
* Simple Neural Network
  - if your intuition says, we can just apply a linReg, then you would be right
    * in a way, you just built your first neural network (w/ an identity activation)
  - but can get fancier, e.g., we know price can never be negative
  - so, for example, can define any house w/ size < s to have price 0
  - this is a simple neural network: it has one neuron, N = xLA
    * that is, the univariate input layer, x, is linearly transformed, z=xL, and activated, y=zA
  
* Relu (REctified Linear Units)
  - the threshold on house size is similar to a step function
    * step(x-s) = {0, x-s < 0; 1, x-s >= 0}
  - in fact, it's like we multiplied the linear equation by a step function
    * f(x) = step(x-s)*line(x)
  - this can be rewritten as a relu function
    * f(x) = max(0, line(x))
  
 * Wider Neural Networks
  - the simplest increase in complexity is to use a wider input layer
  - we can also widen that second layer: just stack neurons like the one we built 
    * 
    * but this would be a vectorial output, so we can add one additional layer -- call it the output layer
    * in the image, Ng shows examples in the hidden layer, but that is to just give you an idea of how the network might combine variables to extract relevant info
      - the hidden layer is determined by the network coefficients which is optimized during training
    * we say that the hidden layer is fully/densely connected b/c each neuron is connected to every input feature 
    
    
 The Hype
  * some of it is justified
  * the only real economic value has derived from applications of DL to supervised learning
    - online advertising has been most lucrative application of neural networks
    - applications to computer vision (e.g., photo tagging) has also been a practical application
    - speech recognition 
    - machine translation (e.g., English to Chinese)
    - autonomous driving
  * a lot of power of DL/SL is cleverly choosing what should be x, what should be y
  
Structured and Unstructured Data
  * structured: most of the stuff (each feature is well-defined)
  * unstructured: audio, images, text 
    - DL has really helped here (in that before DL, this stuff was not always possible)
  
 Scale drivers DL progress
 * note that in the small data regime, hand-crafting features often dominates the NN approach
 * the dominant driver theoretically has been the amount of data (see figure)
 * however, in practice, this driver was only realizable with the rise of compute power (e.g., parallel processing, GPUs)
 * more recently, refined/new algorithms have driven progress as well
  - e.g., switching from a sigmoid activation to a relu activation
  - sigmoids slow down learning b/c of has near-zero gradients in its saturation regions, however, the gradient for relue is nonzero for all positive values
  - relu make gradient descent work much faster
  
Random note:  in this course, m will denote # of training examples

# Week 2: Basics of NN Programming


# Week 3: One Hidden Layer Networks

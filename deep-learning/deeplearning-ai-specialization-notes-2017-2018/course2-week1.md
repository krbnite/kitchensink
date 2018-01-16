

## Train/Dev/Test Sets
* The Dev set is usually what I'd call the validation set

Ng discusses applied ML as a highly iterative process: e.g., as things currently stand, it is difficult
to know when beginning your project how many hidden layers or which activation functions
will work best (among other considerations, such as learning rate, layer widths, number of inputs, etc).  Ng says that,
from what he has seen, intuitions developed in one discipline/domain often do not transfer out-of-the-box
to another domain, e.g., rules-of-thumb that work in natural language processing might not 
work well in computer vision (etc).

In previous years, using a 60/20/20 split for training, validation/dev, and test was common practice (I often
used 70/15/15).  However, Ng says this ratio should only be used on small data sets up to, say, 10k rows.  For big
data sets, there is no need to hold out 15-20\% of the data for the dev and test sets since there is so much 
data and since a larger training portion can help build a better model.  The dev and test sets just needs to "big enough."
For example., if you have 1M rows, you might just use 10k rows in your dev set and another 10k in the test set, which is a
98/1/1 ratio.  If the data set is 10M rows, this ratio would be 99.8/0.1/0.1.

This is a really good point, and actually something I have not been implementing...so can't say I didn't learn
anything today!

Another common scenario these days is using "mismatched" data sets.  Ng's example is for an app that identifies cats
in pictures.  In this case, you might train your app on cat images found on the web, then validate/test the app on
cat pictures taken with the app.  Ng cautions: make sure the dev and test sets come from the
same distribution (which may differ from the training set).

Are test sets necessary?  The goal of the test set to give an unbiased estimate of final model... Sometimes an
app doesn't need that.  For example, it might continuously train and validate as new data comes in.  In cases
where there is just a training set and development set, the development set is often called the "test set."  Note,
however, that it is not a true, unbiased test set.  Ng doesn't like using "test set" in this scenario and strongly
encourages students to go forward referring to this 2-set scenario as one having a training and dev set.  This
practice is only ok if you do not need an unbiased estimate of the performance of your algorithm.


## Bias / Variance 
Ng says: all exceptional practitioners of applied machine learning seem to have a sophisticated understanding of
model bias and variance.

In the era of DL, Ng says there is less talk of the bias / variance tradeoff.  This is because, despite still
having bias and variance in a DL model, there is less tradeoff between them.  

Reminder: what is model bias and model variance?
<figure>
<img src="/images/bias-variance.png" width="600vw">
</figure>

A model that has high bias is one that is specified quite a bit before even looking at the data, e.g.,
a linear model, which demands the model be linear without establishing if that even makes sense.  This model
is likely to remain fairly similar looking on different training sets.  Too much bias can underfit the data.

A model that has high variance is one that is highly dependent on the training set, i.e., it is not specified
too much before looking at the data as in the case with a linear model.  It lets the training data do the talking,
which can be a good thing if it's not talking too much (overfitting).

Example: If we assume that the human error in identifying whether or not a cat is in a photo is ~0\%, then
the following train/dev set errors correspond to bias and variance in the following ways:

<figure>
<img src="/images/bias-variance-error.png", width="600vw">
</figure>

It is important to note that the above example is true assuming that the optimal (Bayes) error is near 0\%.  If
instead, it was near 15\%, then the "high bias" example would actually be the better model.

You might be asking:  Why would the optimal error not be 0%?

Good question! Think blurry images. In a set of blurry images, would you always be able to identify whether or
not a cat was in an image?  Might you mistake a small dog for a cat?  The idea is that there are cases where
the amount of information available simply isn't good enough for completely eliminating error.

What migt be an example of a high-bias, high-variance model?

This is actually model-building 101: fitting a linear model is stringent, and so often at worst will underfit (high
bias). However, fitting a cubic model might have high bias as well as high variance.  If you use too high a degree of 
polynomial, you can essentially fit the training data perfectly: this model would no longer have a bias problem, but
would have an irresponsibly huge variance problem.  (Note that in statistics, a polynomial model is still often called
a "linear model" when referring to its coefficients.)

## Basic Recipe for ML
* High bias?  (Diagnostic: training data performance)
  - try a bigger network (almost always helps reduce bias)
  - train longer (doesn't always help, but mostly doesn't hurt)
  - try other NN architectures (might be overkill, but try if the above doesn't work)
* High variance?  (Diagnostic: dev set performance)
  - if you have it, use more data in training set
  - try out regularization method(s)
  - if necessary, try alternative NN architecture(s)

Note that more training data will not help a high-bias problem.  Similarly, using a bigger
network will not help eliminate a a high-variance problem (it could add more variance!).

What about the bias-variance tradeoff?

Not too long ago, we did not have many tools that could affect either bias or variance in 
isolation. But in the modern big data, deep learning era where compuationaly effort and data set
size are no longer big issues, one can often reduce both: using a bigger network can often reduce
bias without much affecting variance (especially when using regularization), while increasing 
the amount of data used can reduce variance without much affecting bias.


## Regularization
If you notice that you have a high-variance problem (e.g., if your model performs significantly different on
the train set than the dev/val set), then regularization is often the best go-to tool (reliable, no extra data necessary).

### Ex: Logistic Regression
In logistic regression (LogReg), one wants to find the parameters (w,b) that minimize the following
cost function:

Cost(w,b) := (1/m) \* SUM{1,m}{L(y[i],p[i])} 

### L2-Regularization
One can add L2-Regularization (sometimes called "weight decay") to this, resulting in an alternative cost function:

J(w,b) := Cost(w,b) + (r/2m)\*dot(w,w)

Note that the bias, b, can be included in the regularization, but Ng says he usually just ignores it
since the number of bias components are generally so few compared to the number of weights.

### L1-Regularization

### Some Comments on these Techniques
In L2Reg, we want to minimize the "hypotenuse" of the weights.  This selects for keeping weights
from vanishing, if possible, as opposed to L1Reg, which rather the weights vanish.

For example, imagine you have 3 weights all set to 1: (1,1,1).  In both L1 and L2 Regularization,
this adds (r/2m)\*3 to the cost (for simplicity, we will just say it adds 3 units to the cost).  What 
minimizes this better: setting one value to 0 or two values to 0.5?

In L1, scenario A (1+1+0=2) and scenario B (1+0.5+0.5) are equivalent. There is no preference.  The
solution is not unique!  In fact, any scenario where the weights reduce the sum by 1 is equivalent,
e.g., scenario C (1+0.25+0.75=2) or scenario D (2/3 + 2/3 + 2/3 = 2).  

However, in L2, scenario A (1+1+0=2) adds more to the cost than scenario B (1+0.25+0.25=1.5), so L2
regularization will select for scenario B, or as said above -- it will select for maintaining nonzero
weights, if possible and where appropriate.

For L1, because there is a lack of preference, we can give it one. For example, we can try to optimize 
for minimizing the number of nonzero weights.  Or, we can choose to keep the top k largest weights, 
zero out the remainders, and (optionally) refit.  Both cases seek out sparsity: L1 is often used as a way to hone in
on the most important weights... You might use L1 first to trim some weights entirely, then apply L2.

When training NNs, Ng says L2 is used so much more often.  (In physics, this is true of the L2 norm too. Or, if
you think of regularization as adding a kinetic energy term to a Lagrangian, then the L2 norm is, in a sense, more
natural.)

### Ex: More General Neural Network
Logistic regression is a single-layer network.  What about a multi-layer network?

Now, without regularization, the cost function looks functionally similar, though having more arguments:

Cost(w^[1], b^[1], ..., w^[L], b^[L]) = (1/m)\* SUM{1,m}{L(y[i],p[i])} 

What type of regularization should we add?

### The Frobenius (L2) Regularization 
Basically, no one calls it Frobenius regularization: it's still called L2 regularization.  However,
it is important to note that the L2 norm used on the weight vector in logistic regression generalizes
to the Frobenius norm of the weight matrices in more general neural networks. In short, on a matrix,
you can have all sorts of L[i,j] norms, and if i=j=2, then L[2,2] is called the Frobenius norm. Both 
can be called a Euclidean norm if you want to use just one name.  

* Reg term over all layers: R(w^[1], ..., w^[L]) = (r/2m)\*SUM{l=1,L}{ ||w^[l]||^2 }
* Frobenius norm at layer l: ||w^[l]||^2 := SUM{i=1,n^[l-1]}SUM{j=1,n^[l]}{ (w[i,j]^[l])^2 }
  - Also (more qunatum mechanical look):  ||w^[l]||^2 = trace(dagger(w)w)
* n^[l] := # nodes in lth layer
* w^[l] is a (n^[l])x(n^[l-1]) dimensional matrix in Ng's columnar feature vector approach
  - As a reminder: 
    * Row Records (TensorFlow, Udacity): x^[l-1]W^[l] + b^[l] --> x^[l]
    * Column Records (Ng): M^[l]u^[l-1] + d^[l] --> u^[l]
   - CONVERSION: 
    * u' = (xW + b)^T = (xW)^T + b^T = (W^T)(x^T) + b^T = Mu + d
    * x' = (Mu + d)^T = (Mu)^T + d^T = (u^T)(M^T) + d^T = xW + b

### How does adding regularization affect backprop?
Notation Reminder: dw^[l] := dJ/dw^[l]

Without regularization:
* We get dw^[l] from backprop
* We are then able to update the weights: w^[l] <- w^[l] - K\*dw^[l]
  - where K is the step size, aka learning rate

With regularization:
* dw^[l] = D + (r/m)w^[l]
  - where D := (dw^[l] w/o reg)
* w^[l] <- w^[l] - K\*dw^[l] 

Actually... The equations just look the same.  You are still computing partial derivatives of a cost function, etc.

Note that w/ regularization, you have:
* w^[l] <- w^[l] - K\*(D + (r/m)w^[l]) = (1-Kr/m)w^[l] - KD

This is why Frobenius/L2 regularization is also called weight decay -- because the weights
are update by first decaying the weight before subtracting KD.

## Why does regularization prevent overfitting?
As I mentioned above, it has to do with reducing the impact of various weights (and, thus, various nodes) within the network,
sometimes nearly zeroing them out completely.  In some forms of L1 regularization, one does completely zero out some 
weights. If all weights stemming from a particular node are dramatically reduced, that node is not allowed to give too
much input into the final decision (output).  Consider an input node whose outgoing weights have all been nearly zeroed 
out: regularization has helped the network identify the lack of impact this input has on the output and has effectively
ensured that it is ignored in your model (as opposed to falsely believing that it is helpful sometimes because of the
particulars of the train set).  

Ng uses this diagram to help students understand a case of extreme regularization, which effectively
turns the the multilayer network into something like a logistic regression:

<figure>
<img src="/images/network-with-regularization.png" widht="600vw">
</figure>

In reality, L2 regularization will not perfectly zero out those nodes, but it demonstrates the
effect of regularization on the network.

Another way to think about it that Ng provided is as linearizing large swaths of the network. Consider
that small weights will result in small units in the next layer, which will likely be within the linear
regime of the activation function.  Since this portion of the network is effectively linear, it cannot
do loopity-loop style overfitting!

<figure>
<img src="/images/regularization-linearization.png" width="600vw">
</figure>

### Word of Warning: Debugging Gradient Descent
One way to make sure gradient descent is working as it should to to plot the cost function
as a function of iteration... When using regularization, you must remember to use the modified
cost function!

## Dropout Regularization
Say you have a large multi-layer network. You know some of the nodes are useless,
but which ones?  

What if you randomly dropped a few nodes from the network and trained the subnet?  Certain
connections between the remaining nodes would appear to be important, while others -- not so 
much.  But maybe the ones that seemed important are actually way less important than some of
the nodes that you dropped... Well, that's ok.  Just record the weights, and do it all over 
again: generate another random subnet. Update those weights. Etc. Etc. Eventually, the weights
that don't matter, won't matter (too much at least), while the ones that do, basically will 
remain strong.

<figure>
<img src="/images/dropout-regularization.png" width="600vw">
</figure>



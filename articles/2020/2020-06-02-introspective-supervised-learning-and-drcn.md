---
title: Introspective Supervised Learning And DRCN
layout: post
tags: deep-learning transfer-learning domain-adaptation time-series sensors wearables human-activity-recognition autoencoders
---

This note preserves a June 2020 idea sketch from my CVB sensor analytics work:
train a model to classify a signal while also forcing part of the network to
reconstruct the original input. A couple of weeks later, Roozbeh pointed me to
Ghifary et al.'s 2016 paper on Deep Reconstruction-Classification Networks
(DRCN), which lived in the same neighborhood of ideas.

So this is not a claim that I invented DRCN. It is a useful historical artifact
because it shows the line of thought I was following: supervised learning,
autoencoding, transfer learning, and domain adaptation all pulling on the same
rope.

## Main Idea

Train a dual-output model where one output is the input itself, as in an
autoencoder, and the other output is a prediction or classification.

This is similar to multi-step supervised-learning approaches where you first do
self-supervised learning, such as an autoencoder, to get a useful encoding and
then move onto a clustering or classification step. Here, though, the
self-supervised learning happens simultaneously with supervised learning.

## Introspective Strided ConvLSTM

Here is the first rough architecture sketch: an introspective strided ConvLSTM
where only the convolutional layers are self-supervised.

```text
------------ Input (T x C) ------------
              |
              v
       ------ Conv1D (T/2 x D) ------
              |
              v
          --- Conv1D (T/4 x E) ---
              |
              v
       Conv1D (T/8 x F) -> LSTM -> LSTM -> Output -> CrossEntropyLoss
          (Bottleneck)
              |
              v
          -- DeConv1D (T/4 x E) --
              |
              v
       ----- DeConv1D (T/2 x D) -----
              |
              v
------------ Input (T x C) ------------
              |
              v
        AutoEncoderLoss
```

And here is the related version where the convolutional layers plus one LSTM
layer are self-supervised:

```text
------------ Input (T x C) ------------
              |
              v
       ------ Conv1D (T/2 x D) ------
              |
              v
          --- Conv1D (T/4 x E) ---
              |
              v
          Conv1D (T/8 x F)
              |
              v
            LSTM  ->  LSTM -> Output -> CrossEntropyLoss
          (Bottleneck)
              |
              v
          Conv1D (T/8 x F)
              |
              v
          -- DeConv1D (T/4 x E) --
              |
              v
       ----- DeConv1D (T/2 x D) -----
              |
              v
------------ Input (T x C) ------------
              |
              v
        AutoEncoderLoss
```

And obviously there is the example where all convolutional and all LSTM layers
are self-supervised.

## Transductive Transfer Learning

This can also be used in transfer learning, including the CVB sensor/HAR
projects I was thinking about at the time.

A typical approach might be to toss several similar datasets into autoencoder
training, where the source datasets have labels, so that a sparse shared
representation is developed. Then, using that shared representation, add a few
additional trainable layers to create a classifier on the source sets. Finally,
apply `shared_representation + classifier` to the unlabeled target dataset.

In the introspective-learning approach, we can do both steps at the same time by
alternating source and target batches, freezing the classifier layers on target
batches.

As an extension, once the classifier gains good accuracy on the source sets, we
can start using high-confidence pseudolabels from the target set by adding a
third batch type to the sequence:

- source with labels
- target without labels
- target with high-confidence pseudolabels

## TISA / ITTL Sketch

Transductive Introspective Supervised Algorithm, or Introspective Transductive
Transfer Learning:

1. Balance and augment the source and target sets.
2. Train on a source batch.
3. Train on a target batch with frozen classifier layers.
4. Repeat steps 2 and 3 until the epoch is complete, then begin a new epoch.
5. Continue until validation accuracy on the source set reaches its maximum,
   using early stopping and saving the best models.
6. Optional extension:
   - apply the network to the target training set
   - collect high-confidence classifications into a pseudolabel set
   - create a pseudo-source set by balancing and augmenting classes in the
     pseudolabel set
   - create a pseudo-target set by balancing and augmenting classes in the
     remaining target set
   - continue the TISA algorithm

Two possible pseudo-batch schedules:

- Method A: pseudo-source batch, pseudo-target batch, source batch, target batch
- Method B: pseudo-source batch, pseudo-target batch

## Homotopic Autoencoder Augmentation

Another related data-augmentation sketch:

1. Train `SourceAE`.
2. Train `TargetAE`.
3. Generate augmented source data.

```text
                 Source
                 Sample
                   |
                   v
             fSourceEncoder
                 /     \
  a * fSourceDecoder + (1 - a) * fTargetDecoder
```

This could augment the training set by creating target-like samples while
retaining the source labels.

## Walking Cadence As Augmentation Context

For HAR and gesture activities such as walking, running, sitting, and clapping,
there are natural ways to augment the data. For example, moderately brisk
walking is about 100 BPM, vigorous walking is about 130 BPM, and jogging is
often said to start around 140 BPM.

Using an average step length of 2.5 feet:

```text
step_length = 2.5 [ft/step]

# Convert mph to ft/min
mph_to_fpm = (5280 [ft/mile]) / (60 [min/hr])
            = 88 [ft * hr / min * mile]

# Convert ft/min to steps/min
conversion = mph_to_fpm / step_length
           = 35.2

# Steps for 2 mph
steps = round(2 * conversion)
      = 70 [steps/min]

# Steps for 3 mph
steps = round(3 * conversion)
      = 106 [steps/min]

# Steps for 4 mph
steps = round(4 * conversion)
      = 141 [steps/min]

# Steps for 5 mph
steps = round(5 * conversion)
      = 176 [steps/min]
```

Once you look deeper into running and jogging, the numbers start to get messy.
For example, I am guessing stride length typically goes down while running
because average runners are said to go about 6.5 mph and get about 170 steps per
minute, which does not correspond exactly to the numbers above.

But the point is that data augmentation can still help: stretching or shrinking
a walking or running activity by plus or minus 5 steps per minute should stay
within the class, for example. Regular walking seems to be between 70 and 100
steps per minute, moderate-to-brisk walking between 100 and 140, jogging around
140 to 155, and running above that.

The rough sketch at the time was:

```text
walking midpoint ~= 85 steps/minute
5 steps ~= 6%

warp_sign = random choice of -1 or 1
warp_term = random value between 4.5% and 7.5%
warp_length = old_length * (1 + warp_sign * warp_term)
```

The implementation sketch below was marked as wrong in the source draft because
both branches were effectively doing the same kind of operation. I am preserving
it here as an honest project note:

```text
if warp_length < old_length:  # cut and stretch
    r = old_length - warp_length
    start = random choice from r - 1
    w = x[start:start + warp_length]
    w = stretch(w, old_length)
else:  # stretch and cut
    r = warp_length - old_length
    start = random choice from r - 1
    w = stretch(x, warp_length)
    w = w[start:start + old_length]
```

## Introspective Siamese Network

Another related sketch was an introspective siamese network:

```text
Training:

Sample1 -> SharedEncoder -> SampleCode1 -> SharedDecoder -> Sample1 -> AutoEncoderLoss
Sample2 -> SharedEncoder -> SampleCode2 -> SharedDecoder -> Sample2 -> AutoEncoderLoss
                                      |
                                      v
                    distance(SampleCode1, SampleCode2)
                                      |
                                      v
       Loss, for example:
       distance(label1, label2) - distance(SampleCode1, SampleCode2)
```

And the transductive version:

```text
Training:

Sample1 -> SharedEncoder -> SampleCode1 -> SharedDecoder -> Sample1 -> AutoEncoderLoss
Sample2 -> SharedEncoder -> SampleCode2 -> SharedDecoder -> Sample2 -> AutoEncoderLoss
                                      |
                                      v
                    distance(SampleCode1, SampleCode2)
                                      |
                                      v
       Loss, for example:
       distance(label1, label2) - distance(SampleCode1, SampleCode2)
```

## Another Rough Approach

One more rough sketch from the source note:

1. Train a source autoencoder.
2. Train a target autoencoder.
3. Train a source-plus-target autoencoder.

Then piece these things together and see what works:

```text
Train:

Source -> FrozenSourceEncoder -> FrozenTargetDecoder -> Classifier <-> Label

Apply Target:

Target -> Classifier
Target -> FrozenTargetEncoder -> FrozenSourceDecoder -> FrozenSourceEncoder -> FrozenTargetDecoder -> Classifier
```

Or:

```text
Train:

Source -> FrozenCombinedEncoder -> FrozenTargetDecoder -> Classifier <-> Label
Source -> FrozenTargetEncoder -> FrozenCombinedDecoder -> ...
```

The source draft ended mid-thought here. That is probably the right place to
leave it: a clear idea was present, but not yet fully expressed.

## Later Reference

On June 19, 2020, Roozbeh pointed me to:

M. Ghifary, W. B. Kleijn, M. Zhang, D. Balduzzi, and W. Li. "Deep
Reconstruction-Classification Networks for Unsupervised Domain Adaptation
(DRCN)", European Conference on Computer Vision (ECCV), 2016.

## Source Note

This article was lightly cleaned from a CVB internal-blog draft originally dated
June 2, 2020, with a June 19, 2020 update. The cleanup removed quarantine notes,
fixed obvious typos, put diagrams into code fences, and added retrospective
framing so the artifact does not overclaim novelty.

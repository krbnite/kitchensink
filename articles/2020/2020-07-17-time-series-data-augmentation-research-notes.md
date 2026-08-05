---
title: Time-Series Data Augmentation Research Notes
layout: post
tags: time-series data-augmentation sensors wearables human-activity-recognition deep-learning
---

This note preserves July 2020 research notes behind a planned overview of data
augmentation techniques for sensor time series and human activity recognition.
It is best read alongside the three notebook-derived notes on nudged Box-Cox
augmentation, homotopic augmentation, and realistic noise-injection levels.

## Data Augmentation Goal

```text
Sensor Time Series Classification: Data Augmentation: an Overview of the
Do's and Do Not's for Deep Learning Time Series Models

1. finish several literature reviews related to the project;
2. further experiment with and develop various techniques, recording progress
   and results in Jupyter notebooks;
3. develop draft of corresponding paper;
4. submit paper for publication by end of year;
5. write up less technical blog post about the paper for CVB website;
6. share cleaned-up code publicly;
7. encourage CVB communications team to promote the work;
8. have work presented at a conference by Kevin and/or Roozbeh.
```

The gist:

Computer vision and language models rule the world of deep learning. Though
general time series applications are becoming more and more mainstream, there is
still a scarcity of overview and review articles on the peculiarities of time
series. Data augmentation techniques are invaluable in computer vision
applications: random rotations, inversions, scalings, occultations,
discoloration, and more can help yield incredible generalization power.
Unfortunately, the same techniques cannot be blindly applied to time-series
data.

In this project, we develop and overview data augmentation techniques, such as
dynamic time warping, auto-encoded synthetic data, and the application of noise
injection, dropout, and/or batch normalization at input, that help deep learning
models trained on time-series data generalize better on unseen data streams.

We examine the performance of the augmentation techniques on:

- the apnea data set from our previous paper
- CVB's in-house gestures data set
- several publicly available human activity recognition datasets

## Technique Families

The journal listed these known or proposed augmentation families:

- noise injection at input
- batch normalization at input
- dropout at input
- occlusions
- random rotations for multi-axis sensors
- deterministic/meaningful rotations
- random amplitude warping
- functional amplitude warping
- dynamic time warping
- auto-encoded synthetic data
- adversarial/GAN synthetic data

![Synthetic time-series windows used in the July 16 noise-level notebook](../assets/images/2020-07-17-time-series-data-augmentation-research-notes/synthetic-windowed-series.png)

## Potentially Novel Augmentations

I wanted to contribute some novel ideas to this field. For each idea below, it
may or may not be pre-existing; we would have to check. Each of these was
recorded somewhere in my work notebook or one of our repos, documenting and
timestamping it.

- auto-encoded homotopies
  - basically, the gist is that you can formulate homotopy equations between
    activity types, or classes in general; to generate augmented data, you can
    then encode a data point, say of class A, slightly transform the encoding in
    the homotopic direction of another class, say 10% towards class B, then
    decode it and still consider it class A
- nudged Box-Cox augmentations
  - several variants
- frequency-domain distortions
  - phase noise injection
  - amplitude noise injection
  - functional amplitude warping, e.g. slowly decaying/growing factor over
    frequency
  - functional frequency warping, e.g. compress and/or dilate various frequency
    bands, interpolate, and re-index as if they were original frequency indices
  - light amplitude and/or phase dropout
  - amplitude and/or phase occlusion
  - discoloration/recoloration, e.g. perturb the power law in log-log domain

I may have had a few more laying around. Importantly, I had not seen these being
used. That said, I was going to bet the homotopy idea had already been done in
computer vision, but quite possibly not time-series classification. I also
imagined some of the frequency-domain stuff had to have been touched upon. But
we would have to vet it.

## Quick Recap Of Um2017

Quick, efficient definitions for augmentation operations found in Um et al.
(2017):

- **Jitter**: add independent noise samples from `N(0, sigma=0.05)` to each
  `(timestep, channel)` value.
- **Scaling**: for each channel, amplify/attenuate the channel by randomly
  selecting a factor from `N(1, sigma=0.1)`.
- **Magnitude Warping**: for each channel, generate a slowly-varying curve in
  the neighborhood of 1 that has the same number of timesteps as the original
  signal, then multiply it pointwise against the channel signal so that the
  signal is distorted in a smoothly-varying manner.
- **Time Warping**: for each channel, compute the partial sum sequence of a
  randomly generated cubic spline, normalize it so it ranges between `0` and
  `N-1`, like the original time index, then interpolate the associated channel
  values at the fractional indices, resulting in a new `N`-point time series
  that is locally compressed or dilated in the neighborhood of each point.
- **Rotation**: for `C` channels, randomly select a `C`-dimensional rotation
  axis and an angle to rotate the channel data about that axis.
- **Permutation**: given a minimum subinterval length and number of
  subintervals, randomly select and sort cut points, then randomly permute these
  subintervals.

Source paper and code:

- Paper: <https://mediatum.ub.tum.de/doc/1439886/file.pdf>
- GitHub code: <https://github.com/terryum/Data-Augmentation-For-Wearable-Sensor-Data>

## Data Augmentation As Feature Engineering

Insightful note from Hauberg2016:

> Most augmentation schemes "rely on manual specification of the applied transformations, making data augmentation an implicit form of feature engineering," which is contrary to common claims of end-to-end learning models that use these methods.

I wanted to say something like this in our data augmentation review/development
paper: most augmentation schemes rely on manual specification of the applied
transformations, making data augmentation an implicit form of feature
engineering. This is especially true in the case of time series.

## Code And Library References

Some of the code/library references collected in the research notes:

- [Keras TimeSeriesGenerator](https://keras.io/api/preprocessing/timeseries/)
- [Diffeomorphic Deformations](https://github.com/SkafteNicki/libcpab)
- [Cui2016 MCNN code](https://www.cse.wustl.edu/~z.cui/projects/mcnn/)
- [AgaMiko data augmentation review](https://github.com/AgaMiko/data-augmentation-review)
- [Data Augmentation for Audio](https://medium.com/@makcedward/data-augmentation-for-audio-76912b01fdf6)
- [Fast AutoAugment](http://papers.nips.cc/paper/8892-fast-autoaugment)
- [`tsaug`](https://github.com/arundo/tsaug)

## HAR Support Notebook

A companion setup notebook in the same archive used the UCI HAR smartphone
dataset, loaded windows into `(batch, timesteps, channels)` shape, and sketched a
TensorFlow/Keras encoder-decoder model. That notebook also included notes on
Neural Structured Learning examples as possible inspiration for sensor datasets.

```python
def add_channel_dim(x):
    return x[..., np.newaxis]
```

```python
def z_score(in_trn, in_val, in_tst):
    trn_mean = in_trn.mean()
    trn_std = in_trn.std()
    out_trn = (in_trn - trn_mean) / trn_std
    out_val = (in_val - trn_mean) / trn_std
    out_tst = (in_tst - trn_mean) / trn_std
    return out_trn, out_val, out_tst
```

```python
import tensorflow as tf

timesteps = x_trn.shape[1]
channels = x_trn.shape[2]
conv_filters = [8, 16, 32]
cnn_kernel_size = 3
cnn_strides = 2
lstm_dims = [32, 16]

inputs = tf.keras.Input((timesteps, channels), name="input")
x = inputs
for filt in conv_filters:
    x = tf.keras.layers.Conv1D(
        filters=filt,
        kernel_size=cnn_kernel_size,
        strides=cnn_strides,
        activation="relu",
        padding="same",
    )(x)
for dim in lstm_dims:
    x = tf.keras.layers.LSTM(dim, return_sequences=True)(x)
z = x
```

The support notebook was exploratory and was not the main data-augmentation
argument. The Neural Structured Learning work did not become a completed NSL
implementation here, but the setup notebook is part of the same 2020 sensor/HAR
context.

## Source Note

Curated in 2026 from `journal/kevins-data-augmentation-journal.md`,
`references/data-augmentation-references.md`, and
`notebooks/har-with-smartphones_20200617.ipynb` in the standalone
`time-series-data-augmentation` archive. The July 17 date reflects the follow-up
journal/reference commits that consolidated the research notes after the July
13-16 notebooks.

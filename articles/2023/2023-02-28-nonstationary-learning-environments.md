---
title: Nonstationary Learning Environments
layout: post
tags: machine-learning concept-drift transfer-learning domain-adaptation online-learning
---

This short note preserves a February 2023 scratchpad on nonstationary learning
environments, concept drift, transfer learning, and domain adaptation.

The useful little insight here is taxonomic: I had usually treated domain
adaptation as a subset of transfer learning, but the survey I was reading framed
both transfer learning and domain adaptation as special cases of learning under
nonstationarity. That is a good mental model for production ML, where the
question is often not just "can this model learn?" but "what happens when the
world starts moving?"

Source paper:

- [Learning in Nonstationary Environments: A Survey](https://alippi.faculty.polimi.it/articoli/LNSE_survey.pdf)

## Concept Drift

Notes and terms:

- test-then-train scenario
- verification latency
- initially-labeled environments
- hidden context, or perceived drift

From the survey:

> Transfer learning addresses the issue that training and future data must be in
> the same feature space, and have the same distribution. In domain adaptation,
> training and test data are sampled from different but related domains.

I have always considered domain adaptation a subset of transfer learning. These
authors say that both are subsets of nonstationary learning. In a way, what they
call nonstationary learning is what I might call "continuous transfer learning,"
or something like that.

## Adaptation Algorithms

Adaptation algorithms for dealing with concept drift:

- active: aims to detect drift, then issue a model update
- passive: updates whenever there is new data

How to choose active or passive adaptation:

- drift rate
- online data or batches
- computational resources
- assumptions that can be made about the data distributions

Passive approaches:

- gradual drifts, where change detection is difficult
- recurring concepts
- batch settings

Active approaches:

- abrupt drift
- batch or online settings

## Active Detection Sketch

```text
Active Detection of Concept Drift     ^
 |----------------------------------<-|
 |      _____________   Update/       | Classifier Output
 |     | Adaptation  |  Rebuild  _____|______
 |      ------------- --------->|            |
 |           ^                  |            |
 |           | Detected         | Classifier |
 | Error     | Change           |            |
 v      _________________       |            |
 v --->| Change Detector |       ------------
 ^      -----------------            ^
 ^             ^                     |
 |             | Features for        | Features for
 |             | Change Detection    | Classification
 |         ____|_____________________|___
 |        |       Feature Extraction     |
 |         ------------------------------
 |
 |            _________________________
 |___________| Data Generating Process |
              -------------------------
```

## Source Note

This article was lightly cleaned from an untracked draft in the old
`krbnite.github.io` repository:

`_in_progress/2023-02-28-Nonstationary-Learning-Environments.md`

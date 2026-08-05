# Time-Series Augmentation And Local Variation

Reminder created: 2026-08-05

Historical source period: July 2020 CVB data-augmentation notebooks, journal
entries, and paper-planning notes.

## Core Reminder

There may still be a publishable thread in the 2020 time-series augmentation
work, especially the argument that Gaussian noise injection for sensor time
series should be calibrated to local variation rather than global window
variance.

The framing should be modest and precise:

> How much noise is too much? Calibrating time-series augmentation by local
> variation.

This should not be framed as "brand new data augmentation methods." Several of
the old ideas now have close relatives in the literature. The stronger story is
that the 2020 notes independently anticipated practical questions that later
became important: augmentation intensity, label preservation, local similarity,
and spectral preservation.

## Candidate Contribution

A good first publishable shape would be a reproducible benchmark article/repo:

- compare common HAR/time-series augmentations against no augmentation
- rerun classic jitter/noise levels from the literature
- add local-first-difference noise calibration as a simple alternative
- include homotopic / intra-class interpolation as a secondary comparison
- include nudged Box-Cox / monotone power-transform perturbations if they still
  look conceptually clean
- evaluate whether the local-noise rule improves performance, stability, or
  avoids obviously destructive perturbations

Best first outlet: blog article plus reproducible benchmark repo. Consider a
short arXiv-style note only if the experiments are strong.

## Old Ideas And Current Names

| 2020 idea | Closest current/literature language |
|---|---|
| Homotopic augmentation between same-class signals | mixup, intra-class mixup, interpolation-based augmentation |
| Partial / multi-partial homotopies | CutMix-style time-series mixing, segment mixing, local similarity mixing |
| Circularized time-series shifts | time shifting, rolling/cyclic shift, translation-invariance augmentation |
| Frequency-domain distortions | Fourier augmentation, amplitude/phase perturbation, spectral masking |
| First-difference noise calibration | adaptive jitter/noise strength, augmentation intensity, local-similarity-aware augmentation |
| Nudged Box-Cox perturbations | power-transform augmentation, monotone amplitude transformations |

## Literature To Recheck

- [mixup: Beyond Empirical Risk Minimization](https://arxiv.org/abs/1710.09412)
- [SpecAugment](https://arxiv.org/abs/1904.08779)
- [An empirical survey of data augmentation for time series classification with neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0254841)
- [Data Augmentation Techniques in Time Series Domain: A Survey and Taxonomy](https://link.springer.com/article/10.1007/s00521-023-08459-3)
- [SimMix: Local similarity-aware data augmentation for time series](https://www.sciencedirect.com/science/article/pii/S0957417424016609)
- [SimPSI: A Simple Strategy to Preserve Spectral Information in Time Series Data Augmentation](https://ojs.aaai.org/index.php/AAAI/article/view/29405)
- [Time-Series Data Augmentation based on Interpolation](https://www.sciencedirect.com/science/article/pii/S1877050920316914)
- [Data augmentation of wearable sensor data for Parkinson's disease monitoring using convolutional neural networks](https://doi.org/10.1145/3136755.3136817)
- [Impact of Box-Cox Transformation on Machine-Learning Algorithms](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.877569/full)

## Local Sources

Standalone project archive:

- `/Users/kevin/github/CVB/time-series-data-augmentation`

Kitchensink index:

- [Time Series Data Augmentation](../../../time-series/time-series-data-augmentation/README.md)

Related articles:

- [Nudged Box-Cox Time-Series Augmentation](../../../articles/2020/2020-07-13-nudged-box-cox-time-series-augmentation.md)
- [Homotopic Time-Series Augmentations](../../../articles/2020/2020-07-15-homotopic-time-series-augmentations.md)
- [Realistic Noise Injection For Time Series](../../../articles/2020/2020-07-16-realistic-noise-injection-for-time-series.md)
- [Time-Series Data Augmentation Research Notes](../../../articles/2020/2020-07-17-time-series-data-augmentation-research-notes.md)

Ignored quarantine fragments:

- `articles/quarantine/cvb/source-fragments/time-series-data-augmentation/2020-07-16-data-augmentation-project-history-source-fragment.md`
- `articles/quarantine/cvb/source-fragments/time-series-data-augmentation/2020-07-16-experimental-data-augmentation-source-fragment.md`

## Things Not To Overclaim

- Do not claim homotopic augmentation is new without a careful mixup and
  time-series interpolation review.
- Do not claim frequency-domain augmentation is new; the field now has multiple
  amplitude, phase, masking, and spectral-preservation methods.
- Do not claim local-noise calibration is wholly new until checking recent work
  on local similarity, adaptive jittering, and augmentation intensity.
- Do claim the historical evidence accurately: these notes existed in July 2020
  and show independent reasoning about local variation, label preservation, and
  physically plausible sensor augmentation.

## Next Pass

1. Turn the existing 2020 article sequence into a single benchmark plan.
2. Pick 2-3 public datasets: UCI HAR, OPPORTUNITY, and maybe one UCR/UEA
   dataset for generality.
3. Implement a small augmentation library with fixed seeds and visual sanity
   checks.
4. Run baseline comparisons with simple CNN/LSTM/InceptionTime-style models or a
   modern time-series classifier.
5. Decide whether the result is best as a blog article, repo, or short paper.


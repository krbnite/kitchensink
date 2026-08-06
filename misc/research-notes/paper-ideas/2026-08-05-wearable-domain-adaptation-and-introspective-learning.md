# Wearable Domain Adaptation And Introspective Learning

Reminder created: 2026-08-05

Historical source period: June-July 2020 CVB notes on introspective supervised
learning, DRCN, transfer learning, data augmentation, and dataset similarity for
wearable time series.

## Core Reminder

The June 2020 introspective-learning note probably should not be treated as one
novel architecture. It is more valuable as a cluster of related ideas that could
be turned into a careful research/benchmark article:

> Physically plausible data augmentation and domain adaptation for wearable time
> series.

The key idea is to combine several practical pieces that were being thought
through at the same time:

- source-domain classification plus target-domain reconstruction
- alternating source and target batches
- optional high-confidence pseudolabeling
- dataset/domain similarity checks before transfer
- wearable-specific augmentation constraints, such as cadence-aware warping and
  locally calibrated noise

This could become a publishable article or reproducible benchmark if framed as
a practical synthesis for wearable/HAR data rather than as a brand-new model.

## Why There May Be Something Here

The individual pieces have known relatives:

- DRCN already covered shared encoding with source classification and target
  reconstruction.
- DANN already covered learning features that are useful for the source task but
  less domain-discriminative.
- mixup already covered convex combinations of samples and labels.
- Time-series transfer-learning work already used DTW to choose source datasets.
- Time-series augmentation surveys now classify many related jittering, warping,
  magnitude, pattern-mixing, and generative approaches.

The possible contribution is the wearable-specific assembly:

- make augmentation intensity physically plausible for human motion
- compare augmentation methods using HAR/wearable benchmark datasets
- estimate source-target similarity before attempting transfer
- combine reconstruction/classification and pseudolabeling in a clear baseline
  protocol
- show when these methods help, fail, or create unrealistic sensor examples

That is probably more valuable than trying to claim novelty for any one block.

## Candidate Contribution

A good first version would be a benchmark-style article and repo:

1. Pick public wearable/HAR datasets, such as UCI HAR and OPPORTUNITY.
2. Define source-target splits by subject, device location, or dataset.
3. Implement simple baselines:
   - no transfer
   - source-only transfer
   - fine-tuning
   - DANN-style domain confusion
   - DRCN-style reconstruction/classification
4. Add augmentation baselines:
   - jitter/noise
   - magnitude scaling/warping
   - time warping
   - intra-class interpolation/homotopy
   - cadence-aware warping for walking/running classes
   - local-variation-calibrated noise
5. Add source-target similarity checks:
   - DTW-style dataset similarity
   - proxy A-distance
   - simple embedding-space distances
6. Ask which combinations help, which degrade performance, and whether
   similarity metrics predict useful transfer.

Best first outlet: a public technical article plus reproducible benchmark repo.
Consider a short arXiv-style note only if the benchmark produces a clear,
defensible result.

## Old Ideas And Current Names

| 2020 idea | Closest current/literature language |
|---|---|
| Introspective supervised learning | DRCN-style reconstruction/classification, auxiliary self-supervised loss |
| Alternating source and target batches | unsupervised domain adaptation training schedule |
| Frozen classifier on target batches | target reconstruction with source-task supervision |
| High-confidence target pseudolabels | self-training, pseudolabeling, semi-supervised domain adaptation |
| Homotopic augmentation | mixup, intra-class interpolation, pattern mixing |
| Source encoder plus blended decoders | domain translation / reconstruction-based domain adaptation |
| Introspective siamese network | contrastive learning, siamese metric learning, domain-similarity learning |
| Proxy A-distance notes | domain discrepancy estimation |
| Cadence-aware warping | physiology-aware augmentation, label-preserving temporal deformation |

## Literature To Recheck

- [Deep Reconstruction-Classification Networks for Unsupervised Domain Adaptation](https://arxiv.org/abs/1607.03516)
- [Domain-Adversarial Training of Neural Networks](https://jmlr.org/papers/v17/15-239.html)
- [mixup: Beyond Empirical Risk Minimization](https://arxiv.org/abs/1710.09412)
- [Transfer learning for time series classification](https://arxiv.org/abs/1811.01533)
- [Transfer Learning for Activity Recognition: A Survey](https://pmc.ncbi.nlm.nih.gov/articles/PMC3768027/)
- [Time Series Data Augmentation for Deep Learning: A Survey](https://www.ijcai.org/proceedings/2021/631)
- [A comprehensive survey and comparative analysis of time series data augmentation in medical wearable computing](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0315343)
- [A systematic study of unsupervised domain adaptation for robust human-activity recognition](https://doi.org/10.1145/3380985)

## Local Sources

Published kitchensink article:

- [Introspective Supervised Learning And DRCN](../../../articles/2020/2020-06-02-introspective-supervised-learning-and-drcn.md)

Standalone project archives:

- `/Users/kevin/github/CVB/time-series-domain-adaptation-notes`
- `/Users/kevin/github/CVB/sensor-domain-adaptation-and-dataset-similarity`
- `/Users/kevin/github/CVB/time-series-data-augmentation`

Kitchensink indexes:

- [Time-Series Domain Adaptation Notes](../../../time-series/time-series-domain-adaptation-notes/README.md)
- [Sensor Domain Adaptation And Dataset Similarity](../../../time-series/sensor-domain-adaptation-and-dataset-similarity/README.md)
- [Time-Series Data Augmentation](../../../time-series/time-series-data-augmentation/README.md)

Related article-topic guide:

- [Transfer Learning and Domain Adaptation](../../../articles/topics/transfer-learning.md)

## Things Not To Overclaim

- Do not claim reconstruction plus classification is new; DRCN predates the
  2020 note.
- Do not claim adversarial domain adaptation is new; DANN and related methods
  are established baselines.
- Do not claim convex/homotopic interpolation is new without careful comparison
  to mixup and time-series pattern-mixing methods.
- Do not claim DTW-based source selection is new; time-series transfer-learning
  papers already used DTW for dataset similarity.
- Do claim the historical evidence accurately: the June-July 2020 notes show
  independent, applied reasoning about how to make domain adaptation and
  augmentation practical for wearable sensor data.

## Next Pass

1. Decide whether this should become one benchmark repo or two smaller articles:
   one on wearable augmentation and one on domain adaptation/source selection.
2. Build a small literature table mapping each 2020 idea to prior and later
   related work.
3. Audit the existing notebooks for executable code and reusable figures.
4. Pick public datasets and a small model family before writing any grand claims.
5. Let the experiments decide whether the result is a blog article, benchmark
   repo, or short paper.

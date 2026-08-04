# Fungus Amongus, 2017

This is a 2017 decision-tree notebook built around the UCI mushroom dataset. It is preserved here as a learning artifact rather than a polished, modernized project.

The notebook's name is based on an Inucubus album, and its theme is Treebeard deciding whether a mushroom is poisonous...because
these things were cool to me in 2017 -- and they still are, in 2026.

## Files

- `Decision-Trees-in-Sklearn.ipynb`: the original notebook.
- `assets/Treebeard.jpg`: image used by the notebook.

## Historical Context

The imported git history records this work as August 1-3, 2017:

| Commit | Author Date | Subject |
| --- | --- | --- |
| `a50a983` | `2017-08-01T18:35:51-04:00` | `Create Decision Trees notebook` |
| `fd6245c` | `2017-08-01T21:09:18-04:00` | `Add Treebeard stuff` |
| `24a6cd0` | `2017-08-02T11:31:00-04:00` | `Add bits about feature selection and dimensionality reduction` |
| `b7c0491` | `2017-08-02T11:39:59-04:00` | `Minor updates to Treebeard notebook` |
| `d736b43` | `2017-08-02T13:55:58-04:00` | `Add bit about linear discriminant analysis` |
| `118f4cb` | `2017-08-03T10:30:54-04:00` | `Add bit about random_state in DecisionTrees NB` |
| `e7e2953` | `2017-08-03T15:31:04-04:00` | `Add intro to DTs NB` |

The filesystem timestamps may reflect the 2026 kitchensink import, but the git history preserves the original 2017 dates.

## What It Covers

The notebook is a loose walkthrough of decision trees in scikit-learn:

- decision trees as nonparametric supervised models
- Gini impurity vs. entropy/information gain
- train/validation/test splitting
- random state sensitivity
- one-hot encoding categorical variables for scikit-learn
- feature selection with chi-squared, ANOVA F-values, and mutual information
- multicollinearity checks
- PCA vs. LDA as dimensionality reduction before a classifier
- F1 score comparisons on poisonous vs. edible mushrooms

It also has the notebook voice of its era: jokes, rough edges, exploratory cells, and a few conclusions that would deserve a more careful rerun before being treated as final analysis.

## Data

The notebook expects these UCI mushroom dataset files to exist beside the notebook:

- `agaricus-lepiota.names`
- `agaricus-lepiota.data`
- `feature_names.txt`

Those files are not currently checked into this folder. The notebook includes old shell commands for fetching and preparing them:

```python
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
!cat agaricus-lepiota.names | grep "^[[:space:]]\\{4,5\\}[0-9]\\{1,2\\}.*:" > feature_names.txt
```

On macOS, `wget` may not be installed by default. Use `curl -O` instead, or run the notebook in an environment where `wget` is available.

## Reproducibility Notes

This notebook was created with Python 3.6-era tooling. The notebook imports:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib` through notebook inline plotting

If revisiting it (unlikely!), expect to update some scikit-learn behavior, pin package versions, and decide whether to preserve the original exploratory results or rerun everything cleanly.

## Why Keep It at All?

It belongs in kitchensink because it captures the some of the learning process as it actually looked: curious, messy, funny, and technical enough to be worth preserving.

## Related Historical Articles

This short blog post points back to the same 2017 mushroom decision-tree notebook. The broader tree-model article index lives in `../README.md`.

- [Treebeard and the Fungus Amongus: Exploring Decision Trees in Scikit Learn](../../articles/2017/2017-08-03-Treebeard-and-the-Fungus-Amongus.md) (2017-08-03)

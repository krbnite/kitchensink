# Notebooks

This folder is the canonical archive for standalone notebook artifacts.

The organizing rule is intentionally simple: notebooks that are basically self-contained historical artifacts live here, while notebooks that belong to a fuller mini-project stay with their project folder, README, environment setup, inputs, outputs, or supporting code.

## Contents

- [Curation Pattern](#curation-pattern)
- [Standalone Notebooks](#standalone-notebooks)
- [Project Notebook Index](#project-notebook-index)

## Curation Pattern

- Use `notebooks/YYYY/` for notebook-only artifacts imported from older repos or folders.
- Keep notebooks inside topic/project folders when they depend on a local project structure.
- Link notebooks from relevant topic READMEs rather than duplicating files across topics.
- Preserve Git history when importing or moving notebook artifacts whenever practical.

## Standalone Notebooks

These notebooks are kept as historical working evidence. They may include output cells, scratch-style exploration, and old dependency assumptions.

### 2019

- [Next Point Forecast with Random Forest](2019/2019-09-13-next-point-forecast-with-random-forest.ipynb): synthetic time-series next-point forecasting with random forests, memory-efficient rolling windows, different input window sizes, and basic accuracy/runtime exploration.
- [Stabilizing Variable Importance Fluctuations in Random Forests](2019/2019-09-22-stabilizing-variable-importance-fluctuations-in-random-forests.ipynb): early experiment around stabilizing random-forest feature-importance estimates, motivated by a paper on variable-selection stability.

These two notebooks were imported from the old `krbnite.github.io/_notebooks` folder. Their preserved Git history runs from September 13, 2019 through November 12, 2019. The original folder also contained an `Untitled.ipynb` file, but that notebook had one empty code cell and no outputs, so it was intentionally omitted.

The notebooks were written against a 2019 Python/scikit-learn stack and may need small dependency or syntax updates in a modern environment. Expected packages include:

- `numpy`
- `pandas`
- `scipy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `scitime`

The variable-importance notebook downloads UCI mushroom data into a local `_data/` folder. That folder remains ignored by Git in `notebooks/2019/.gitignore`, matching the original notebook directory.

Related articles:

- [Random Forests and Tree Ensemble Research Notes](../articles/2019/2019-03-29-random-forests-and-tree-ensemble-research-notes.md) (2019-03-29)
- [The Quest for Blackbox Interpretability](../articles/2019/2019-06-12-the-quest-for-blackbox-interpretability.md) (2019-06-12)
- [The Quest for Blackbox Interpretability (Take 1, Random Forests and Feature Importances)](../articles/2019/2019-06-21-The-Quest-for-Blackbox-Interpretability-Take-1.md) (2019-06-21)
- [Time Series Forecasting with a Random Forest (1 of N)](../articles/2019/2019-09-13-Time-Series-Forecasting-with-Random-Forests-1-of-N.md) (2019-09-13)
- [Variable Importance Assessment in Random Forest Regressions](../articles/2019/2019-09-13-Variable-Importance-Assessment-in-Random-Forest-Regressions.md) (2019-09-13)
- [Experimenting with Random Forests on UCI ML Data Sets](../articles/2019/2019-09-25-Experimenting-with-Random-Forests-on-UCI-ML-Data-Sets.md) (2019-09-25)

## Project Notebook Index

These notebooks are intentionally left with their surrounding projects because the README, environment setup, data notes, support scripts, or imported course/project structure provide useful context.

- [Bayesian Statistics Snippets](../bayes/bayesian-stats.ipynb): compact notebook of Bayesian probability and log-odds examples.
- [Gradient Inspection Notes](../deep-learning/gradients/README.md): 2020 TensorFlow gradient-inspection notebook plus modern TensorFlow/PyTorch companion.
- [NumPy Neural Network From Scratch](../deep-learning/numpy-neural-network-from-scratch-2017/README.md): standalone reconstruction of 2017 neural-network derivation and NumPy implementation work.
- [Udacity Deep Learning Nanodegree Foundation](../deep-learning/udacity-dlnd-2017/README.md): preserved 2017 deep-learning notebooks and project artifacts.
- [Word Embeddings Notes](../nlp/word-embeddings/README.md): cleaned 2018-era NLP notebook covering WordNet, one-hot vectors, co-occurrence vectors, cosine similarity, and SVD.
- [BillyBot Legacy](../nlp/chatbots/billybot2017/README.md): preserved 2017 rule-based chatbot notebook.
- [Self-Driving Car Nanodegree 2017](../robotics/self-driving-car-nanodegree-2017/README.md): preserved autonomous-vehicle notebooks and mini-project artifacts.
- [Fungus Amongus 2017](../trees/fungus-amongus-2017/README.md): preserved mushroom decision-tree notebook with supporting article/context.
- [FastSAM 2024 Notebook](../vision/fastsam2024/README.md): preserved segmentation notebook with environment setup, local output handling, and implementation notes.

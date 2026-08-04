# Random Forest Notebooks 2019

Preserved Jupyter notebooks from the old `krbnite.github.io/_notebooks` folder.

These notebooks are kept as historical random-forest experiments from September 2019. They are not polished tutorials or guaranteed-rerunnable environments, but they connect directly to the article trail around random forests, time-series forecasting, feature importance, and black-box interpretability.

## Contents

- [Notebook Map](#notebook-map)
- [Historical Status](#historical-status)
- [Data and Runtime Notes](#data-and-runtime-notes)
- [Related Articles](#related-articles)

## Notebook Map

- [2019-09-13-Next-Point-Forecast-with-RF.ipynb](2019-09-13-Next-Point-Forecast-with-RF.ipynb): synthetic time-series next-point forecasting with random forests, memory-efficient rolling windows, different input window sizes, and basic accuracy/runtime exploration.
- [2019-09-22-Stabilizing-Variable-Importance-Fluctuations-in-a-Random-Forest.ipynb](2019-09-22-Stabilizing-Variable-Importance-Fluctuations-in-a-Random-Forest.ipynb): early experiment around stabilizing random-forest feature-importance estimates, motivated by a paper on variable-selection stability.

## Historical Status

The preserved Git history for these notebooks runs from September 13, 2019 through November 12, 2019. The original website folder also contained an `Untitled.ipynb` file, but that notebook had one empty code cell and no outputs, so it was intentionally omitted.

This folder is preserved as notebook-era working evidence. The notebooks still include output cells and scratch-style exploration.

## Data and Runtime Notes

The notebooks were written against a 2019 Python/scikit-learn stack and may need small dependency or syntax updates in a modern environment.

Expected packages include:

- `numpy`
- `pandas`
- `scipy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `scitime`

The variable-importance notebook downloads UCI mushroom data into a local `_data/` folder. That folder remains ignored by Git, matching the original notebook directory.

## Related Articles

- [Random Forests and Tree Ensemble Research Notes](../../articles/2019/2019-03-29-random-forests-and-tree-ensemble-research-notes.md) (2019-03-29)
- [The Quest for Blackbox Interpretability](../../articles/2019/2019-06-12-the-quest-for-blackbox-interpretability.md) (2019-06-12)
- [The Quest for Blackbox Interpretability (Take 1, Random Forests and Feature Importances)](../../articles/2019/2019-06-21-The-Quest-for-Blackbox-Interpretability-Take-1.md) (2019-06-21)
- [Time Series Forecasting with a Random Forest (1 of N)](../../articles/2019/2019-09-13-Time-Series-Forecasting-with-Random-Forests-1-of-N.md) (2019-09-13)
- [Variable Importance Assessment in Random Forest Regressions](../../articles/2019/2019-09-13-Variable-Importance-Assessment-in-Random-Forest-Regressions.md) (2019-09-13)
- [Experimenting with Random Forests on UCI ML Data Sets](../../articles/2019/2019-09-25-Experimenting-with-Random-Forests-on-UCI-ML-Data-Sets.md) (2019-09-25)

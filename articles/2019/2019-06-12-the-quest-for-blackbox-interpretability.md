# The Quest for Blackbox Interpretability

> Historical note: Curated in 2026 from draft notes originally committed in `krbnite.github.io` from 2019-06-12 to 2020-01-28. The source draft histories were imported into this repository before this consolidation step.
> Curation note: Consolidates the in-progress interpretability sequence. The already-imported Take 1 article remains as a separate historical published draft and is linked below.
> Related published draft: [The Quest for Blackbox Interpretability (Take 1, Random Forests and Feature Importances)](2019-06-21-The-Quest-for-Blackbox-Interpretability-Take-1.md).

## Source Drafts

- `2019-06-12-LIME.md`
- `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-2.md`
- `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-3.md`
- `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-4.md`
- `2019-06-26-The-Quest-for-Blackbox-Interpretability-Take-5-Anchors.md`
- `2019-09-21-Stable-Variable-Importance-Values-in-Random-Forests.md`

## LIME (2019-06-12; source: `2019-06-12-LIME.md`)

* [Understanding model predictions with LIME](https://towardsdatascience.com/understanding-model-predictions-with-lime-a582fdff3a3b)
* [LIME on GitHub](https://github.com/marcotcr/lime)

https://www.oreilly.com/learning/introduction-to-local-interpretable-model-agnostic-explanations-lime

https://towardsdatascience.com/decrypting-your-machine-learning-model-using-lime-5adc035109b5

## The Quest for Blackbox Interpretability (Take 2, PImp and CPImp) (2019-06-19 to 2019-07-08; source: `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-2.md`)

* [Be Aware of Bias in RF Variable Importance Metrics](https://blog.methodsconsultants.com/posts/be-aware-of-bias-in-rf-variable-importance-metrics/)
  - very useful article detailing when Gini importance is ok, when to instead opt for permutation importance, and when to
    upgrade to conditional permutation importance
* [Bias in random forest variable importance measures: Illustrations, sources and a solution](https://link.springer.com/article/10.1186%2F1471-2105-8-25)
  - for when you have to use sampling-without-replacement instead of bootstrapping (sampling-with-replacement)
* [Conditional variable importance for random forests](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2491635/)
  - paper that originally proposed conditional permutation importances
* [Selecting good features – Part III: random forests](http://blog.datadive.net/selecting-good-features-part-iii-random-forests/)
  - Provides short, to-the-point descriptions of Gini and Permutation importances
* [Interpretable Machine Learning: Feature Importance](https://christophm.github.io/interpretable-ml-book/feature-importance.html)
  - From the online book "[Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)"



[Interesting perspective](http://blog.datadive.net/selecting-good-features-part-iii-random-forests/) on permutation
importance:
> "Keep in mind though that these measurements are made only after the model has been trained (and is depending)
> on all of these features. This doesn’t mean that if we train the model without one these feature, the model
> performance will drop by that amount, since other, correlated features can be used instead."

Note that it's also found that correlated predictors are not given their proper importance in permutation
importances since permuting one predictor is less meaningful if a highly correlated predictor exists to
stand in for it....

## The Quest for Blackbox Interpretability (Take 3, LIME) (2019-06-19 to 2019-06-27; source: `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-3.md`)

* [“Why Should I Trust You?” Explaining the Predictions of Any Classifier](https://arxiv.org/pdf/1602.04938.pdf)
  - Original LIME paper
* [Justifying a Random Forest](https://roywright.me/2018/02/09/justifying-random-forest/)
  - Shows an example using LIME
  - Describes some shortcomings of LIME
  - Plugs `treeinterpreter` Python package
  - Shows how he made `treeinterpreter` better / more robust
* [Model-Agnostic Methods: Local Surrogate (LIME)](https://christophm.github.io/interpretable-ml-book/lime.html)
  - From the online book "[Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)"

Crazily enough, I just got an email from Two Sigma with an article that covers exactly the topics I've reading
and writing about for the past week or so:
* https://www.twosigma.com/insights/article/interpretability-methods-in-machine-learning-a-brief-survey



Related:  I saw that there is a Kaggle micro-course on model explainability.  I should check it out:
* https://towardsdatascience.com/why-model-explainability-is-the-next-data-science-superpower-b11b6102a5e0
* https://www.kaggle.com/learn/machine-learning-explainability?utm_medium=blog&utm_source=medium&utm_campaign=medium-learn-explain

## The Quest for Blackbox Interpretability (Take 4, Shapley) (2019-06-19; source: `2019-06-19-The-Quest-for-Blackbox-Interpretability-Take-4.md`)

* [Interpretable Machine Learning: Shapley Values](https://christophm.github.io/interpretable-ml-book/shapley.html)
  - From the online book "[Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
* [An unexpected unity among methods for interpreting model predictions](https://arxiv.org/pdf/1611.07478.pdf)
  - Goes over a generalization of Shapley values that they call "Expectation Shapley values"

## The Quest for Blackbox Interpretability (Take 5, Anchors) (2019-06-26 to 2019-07-02; source: `2019-06-26-The-Quest-for-Blackbox-Interpretability-Take-5-Anchors.md`)

* https://github.com/marcotcr/anchor
* https://homes.cs.washington.edu/~marcotcr/aaai18.pdf



Also: LORE
* https://arxiv.org/abs/1805.10820

## Stable Variable Importance Values in Random Forests (2020-01-28; source: `2019-09-21-Stable-Variable-Importance-Values-in-Random-Forests.md`)

2017: Behnamian et al: [A Systematic Approach for Variable Selection With Random Forests: Achieving
Stable Variable Importance Values](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8038868)
  - We've all been there: train your RF, look at the feature importances.  Maybe you want to find the
    top 10 features to go ahead and make a more computationally efficient model (that also lessens the
    burden of future data collection needs).  Or maybe you just want to better explain the internal
    logic of your model to a stakeholder.  Whatever: the results look interesting, but you decide to
    add more trees and retrain to see if you get better accuracy.  Nice!  You do!  But, wait:
    the imporantces changed rankings.  So you add some more trees, train again -- and again a slightly
    different set of importance rankings.  What's worse: your curiosity gets the best of you and without
    changing any hyperparameters whatsoever, you retrain and get yet a different ranking. It doesn't
    matter if you're using Gini importance (aka mean decrease in impurity) or permutation importance
    (aka mean decrease in accuracy).  Both  prove to be fairly unstable.  What's the deal here?!
  - This paper looks at (i) how large a forest must be to produce stable importance estimates, and
    (ii) how class separability affects this result.
    * They do find that, for large enough nTree, the importances stabilize
    * They also find that averaging the rankings over multiple runs with smaller nTrees produces stable estimate
    * The specifics are driven by the class separability
  - Interestingly, this paper is about the use of RFs in signal and image processing, where the data is
    collected at high temporal and/or spatial frequency.
    * This motivates the need for stable importance rankings: "Reducing model data load can reduce processing
      times and storage requirements, and can also be used to inform longterm analyses, as attention can focus
      on just the sensors and variables that provide relevant information to a given classification problem."
    * Furthermore, in this signal/image analysis field, it has been shown that RFs can be improved quite a
      bit by finding and removing any noise variables.
  - Importantly, independent of what VImp measure one uses, "because of the random way in which training data
    and variables are selected to determine the split at each node in Random Forests, importance rankings
    differ from one model run to another, especially when if only a small ntree are generated."

Jupyter Notebook: https://github.com/krbnite/krbnite.github.io/blob/master/_notebooks/2019-09-22-Stabilizing-Variable-Importance-Fluctuations-in-a-Random-Forest.ipynb

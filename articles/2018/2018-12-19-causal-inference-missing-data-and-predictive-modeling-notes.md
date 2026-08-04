# Causal Inference, Missing Data, and Predictive Modeling Notes

> Historical provenance and source draft details are at [Historical Provenance](#historical-provenance).

## Summary

These notes collect a 2018-2019 thread around causal inference, missing data, categorical feature handling, and the difference between a model that predicts well on historical data and a model that behaves sensibly in live use.

The most useful material is the treatment-intake prediction scenario, the MCAR/MAR/MNAR examples, and the recurring question of what changes once predictions are used to intervene in the system being predicted.

## Contents

- [Causal inference reading notes](#causal-inference-reading-notes)
- [Predictive models and counterfactuals](#predictive-models-for-counterfactuals)
- [Categorical variables and missingness scenario](#categorical-variables-and-missing-values-in-live-models)
- [Feature-type reflections](#reflections-on-feature-types)
- [MCAR, MAR, and MNAR examples](#classifying-circumstances-of-missing-data)
- [Graphical models of missingness](#graphical-models-of-missingness)
- [Prediction-in-practice link notes](#predictive-models-in-practice)

## Causal Inference Reading Notes

NEXT UP:

* Module 2: https://www.coursera.org/lecture/crash-course-in-causality/confounding-VT3H4
  - disjunctive cause criterion can also be called "disconnective criterion" or "simply disconnect criterion"
  since "disjunctive" means "lacking connection" and the criterion basically says "only worry about
  disconnecting nearest neighbor nodes that flow directly into A or Y" (btw, doesn't always work, but good rule of thumb)

* Module 3: https://www.coursera.org/lecture/crash-course-in-causality/observational-studies-V6pDQ

* Module 4: https://www.coursera.org/lecture/crash-course-in-causality/intuition-for-inverse-probability-of-treatment-weighting-iptw-nrrCT

* Module 5: https://www.coursera.org/lecture/crash-course-in-causality/introduction-to-instrumental-variables-ueIMD
  - Ertefaie et al [2017]: [A tutorial on the use of instrumental variables in pharmacoepidemiology](https://www.cceb.med.upenn.edu/sites/default/files/uploads/cter/A%20tutorial%20on%20the%20use%20of%20instrumental_0.pdf)
  - Baiocchi et al [2015]: [Tutorial in Biostatistics: Instrumental Variable Methods for Causal Inference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4201653/)
------------------------

### Misc Reading
* https://en.wikipedia.org/wiki/Causal_inference
* https://en.wikipedia.org/wiki/Rubin_causal_model
* https://en.wikipedia.org/wiki/Instrumental_variables_estimation

http://mlg.eng.cam.ac.uk/zoubin/SALD/Intro-Causal.pdf

https://www.inference.vc/untitled/

http://www.jmlr.org/papers/volume11/spirtes10a/spirtes10a.pdf

https://blog.acolyer.org/2018/09/17/the-seven-tools-of-causal-inference-with-reflections-on-machine-learning/

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.726.5229&rep=rep1&type=pdf


* Chen & Pearl [2013]: [Regression and Causation: A Critical Examination of
Six Econometrics Textbooks](https://ftp.cs.ucla.edu/pub/stat_ser/r395.pdf)
* Saddiki & Balzer [2018]: [A Primer on Causality in Data Science](https://www.researchgate.net/publication/327549882_A_Primer_on_Causality_in_Data_Science)
* Mohan & Pearl [2018]: [Graphical Models for Processing Missing Data](https://ftp.cs.ucla.edu/pub/stat_ser/r473-L.pdf)

Course notes:
* http://bkenkel.com/psci8357/notes/08-causal.pdf
  - points out an interesting thing about causal models: in a regression, you do not want to include
  post-treatment variables, e.g., tar build up in lungs when your treatment is smoking and outcome is lung cancer;
  this is b/c the tar buildup variable will strongly predict the outcome, pushing the coeff on smoking towards
  zero, despite smoking being the cause for both tar build up and the outcome... In a ML predictive model you
  wouldn't care, but in a causal model it matters

--------------------------------

Some Google stuff:

http://www.unofficialgoogledatascience.com/2017/01/causality-in-machine-learning.html

* Google's R Package:  https://opensource.googleblog.com/2014/09/causalimpact-new-open-source-package.html
  - Corresponding paper:  https://ai.google/research/pubs/pub41854

-----------------------------------

Susan Athey (ML + CI)

https://github.com/susanathey/causalTree

https://github.com/swager/causalForest

https://www.coursera.org/learn/statistical-inferences

-----------------------------------

Excellent Medium articles on ML/CI

https://medium.com/teconomics-blog/machine-learning-for-decision-making-e776f9f8917e

https://medium.com/teconomics-blog/using-ml-to-resolve-experiments-faster-bd8053ff602e

https://medium.com/teconomics-blog/machine-learning-meets-instrumental-variables-c8eecf5cec95

------------------------------------


People working on ML+CI

http://www.mit.edu/~vchern/

https://www.gsb.stanford.edu/faculty-research/faculty/susan-athey

https://www.gsb.stanford.edu/faculty-research/faculty/guido-w-imbens

----------------

Potential models to look into:
•	Already looking into:  marginal structural models (MSMs), structural nested models (SNMs), and the g-formula
•	Can also explore:  discontinuity design, difference-in-differences, fixed effects modeling, and instrumental variables modeling

------------------------------------------

Other MOOCs:
* https://www.coursera.org/learn/causal-inference
* https://www.coursera.org/learn/causal-effects
* https://www.coursera.org/learn/probabilistic-graphical-models
* https://www.edx.org/course/causal-diagrams-draw-assumptions-harvardx-ph559x
* https://www.coursera.org/learn/designexperiments

Courses:
* 2019 Columbia Course: http://www.cs.columbia.edu/~blei/seminar/2019-applied-causality/
  - weekly recommended readings (Pearl, Hernan, Robins, etc)
  - should go through the readings

## Predictive Models for Counterfactuals

These exist... Want to learn more!


https://www.oreilly.com/learning/all-the-data-and-still-not-enough

## Categorical Variables and Missing Values in Live Models

## The Scenario

**The Data**:  Let's say you are working with a data set about depressed subjects.  Specifically, you gain some
data at intake about each subject: demographic/socioeconomic (e.g., gender, age, race, income, employment),
criminal (e.g., arrests), drug background (e.g., primary substance of abuse, frequency of abuse, etc), and
maybe even a questionnaire or two is filled out (e.g., PHQ-9, HAM-D).  Sometimes all this information
is available.  Other times, it's not: the patient may skip items on the questionnaire, or it might never
make it to the database.  Maybe they opt to not fill out a bunch of demographic data, etc.

Let's say we have about 5 years of this type of data.

**The Goal**:  We want to estimate at intake whether this person will complete treatment, or dropout.  That is,
we want to deploy a prediction model that takes in the relevant data at intake and provides the clinic with some
estimates (e.g., classify as a dropout or completer, estimate the number of treatments taken before
completion or dropout, etc).  Ideally, uncertainties will be included in these estimates so that the information
can be used intelligently.  Ultimately, the model is guiding the clinic how to prioritize resources (time,
personnel hours, etc), treatment approaches, and so on.

**The Setback**:  Yes, we can create a predictive model given the historical data.  Simple, right?  Just
split the data up in training, validation, and test sets, establish a meaningful model metric, and make a model
that wows in validation, and doesn't disappoint on test.

Except that we go beyond the test set in deployment.  See, on the test set, we just made a prediction, then
checked if we were right.  In deployment, we will also make a prediction, but we will NEVER get to check if we
were right.  This is because in deployment, the intention is to intervene on these predictions -- if someone is
likely to dropout after 2-3 treatments, but needs at least 10, we are likely going to expend more resources
on that subject, hoping to convert a dropout into a completer.  After such an intervention, it is
no longer clear whether your model is bad or your intervention/treatment is really good!

This is where things like A/B testing crop up in marketing: did our email campaign influence more purchases,
and if so can we quantify that?  This, in general, is where causal inference comes into play.

But causal inference is hard, and I'm just trying to write about whether or not we should delete, impute,
or preserve missing values in nominal categorical variables.

So, for sanity's sake, let's assume
no interventions take place for now: we just want to nerd out with the data in hand.  If the model is good on
test, we'll be happy to deploy it.  And in deployment, we will make predictions, but do nothing:  we'll
simply wait to see whether the model is right or wrong.  Kind of like a weather forecast.

Ok, let's focus on missing data.

## The Missing Data
### The Predictor Variables
Also, there is a marriage variable
with the levels: never married, now married, separated, divorced, MISSING/UNKNOWN/NULL.

Should we remove any row with missing data?  Should we somehow impute these categorical variables?  If
so, then how?

It should be no surprise that this is all context-dependent.  Let's dive in...




### The Target Variable
The first discrepancy arises: not everyone fits neatly into our universe of completers and dropouts.  Turns out
that some patients exit treatment for other reasons.  For example, death, incarceration, or relocation. Some
folks are even more mysterious: they reason for exit is MISSING/NULL.

The last reason is classic missing data.   But what of death, incarceration, or relocation?

Comleted case analysis (CCA) would have us remove the missing data.  But what should we do about the
available, but not very straightforward data?



## The Target
We are interested in dropout/retention as an outcome.  Let's say the data set includes a variable,
DISCHARGE_REASON, which has the following levels and percentages:
* CT - completed treatment (48%)
* DO - dropped out prior to completing treatment (29%)
* IN - incarcerated prior to completing treatment (2%)
* DI - died prior to completing treatment (1%)
* RT - relocated/transferred to another facility/location prior to completing treatment (17%)
* UK - UNKNOWN/MISSING/NULL (3%)

What we do has everything to do with our goal: is this patient likely to dropout or complete treatment.

There are a few approaches we can take:
* make this a binary classification problem (CT/DO) and throw out other levels of
  DISCHARGE_REASON before splitting data set into training/validation/test
* make this a multiclass classification problem, e.g., DO/CT/OTHER
* rescope our problem as a completion vs non-completion problem (CT/OTHER)


For example,
we are not trying to predict death.  Since
death does not neatly fit into completion or dropout, I think we can remove them.  Think about the
patient intake process: our goal is to estimate a patient's likelihood of completing treatment.

## Reflections on Feature Types

In statistical data analysis, you will often hear about different types of data, specifically whether
a given feature is nominal, ordinal, interval, or ratio.

I'm here to say that's just the start.

Often, you will encounter variables that I might call partially-ordinal and ratio-like ordinal.

## Partially Ordinal
By "partially ordinal", I mean when you have values like those found in a family tree: say you a variable called
`family_member` with levels "Mom", "Dad", "Johnny", and "Sally Sue".  In terms of family lineage,
* Mom > Johnny
* Mom > Sally Sue
* Dad > Johnny
* Dad > Sally Sue
* But no ordering exists between Johhny and Sally Sue, or Mom and Dad

This can clearly just be considered nominal categorical variable, but nonetheless a partial ordering exists.  Is
there a way to exploit that information better than just dummyizing the variable into 4 binary features?

## Ratio-Like Ordinal
By ratio-like ordinal, I mean an ordinal variable that has a well-defined zero, which is the distinguishing feature
between ratio and interval variables (in fact, in this parlance, you might consider regular "ordinal" to be
called "interval ordinal").

For example, you can have a feature called `number_of_arrests` that is coded like: "none", "one", and "two or more".  With
the raw, granular data, this would be a ratio variable type.  By binning it, it has become ordinal.  But not just
ordinal: it still has a well-defined zero.  This is in contrast to a variable like `temperature` that takes on
the values "super cold", "pretty cold", "meh", "warm", and "hot", which has order, but not necessarily a zero (and
especially not a well-defined zero).

Again, does the existence of this well-defined zero have intrinsic value that can be served by using one
technique over another?

## Classifying Circumstances of Missing Data

When is data missing completely at random (MCAR)? Or conditionally at random (MAR)?  Or not
missing at random (MNAR)?



Scenario 1: Patients are provided with two 10-item questionnaires over the course of a year
to help assess their heart health; a health score is assigned to each.  Aside from the
answers provided and associated health scores, the clinic collects demographic information
on the patients, such as age, income bracket, and health insurance provider.


Scenario 1a: Data is provided to the analyst as an outer join between the two data sets,
resulting in rows of data, where each row represents a patient and depicts their demographic information (if
available) as well as their responses to the questionnaire (if available).

It is found that missing questionnaire data can largely be explained by age: generally speaking, young
patients have no questionnaire data because they were not flagged as needing to fill it out.  After
stratifying by age, we find that there is further dependedence on health insurance provider: patients
with no health insurance are less likely to have filled out the questionnaire. We would
say this missing data is (conditionally) missing at random (MAR).


Scenario 1b:  Data is provided to the analyst as an inner join between the demographic and questionnaire
data sets.  In other words, we now are looking at the population of patients that have been flagged
as questionnaire recipients.

Some patients that are flagged as having filled out a questionnaire do not have any data recorded for one
or both questionnaires.  After some investigation, it is found that every time its Chris' turn to input the data, there
are several missing data files because Chris is lazy and doesn't know WTF he's doing.  We would say that this
data is MCAR.

We also find the number of men and women filling out the questionnaire is about equal, even in the
older age brackets, which does not match the statistics for those who die from heart attack.  It is unclear
if our patient population accurately reflects the true population, e.g., are their less older men in our
patient population because the dead don't go to the doctor, or because these men are already on
heart medication and don't need to fill out the questionnaire?  ... MNAR...?

MNAR:  We also find that it appears more older men are missing the responses and health score for the second
questionnaire, which feels very MAR...but we also notice that the health scores available are suspicously high,
and so we investigate and find that the missing health scores for the second questionnaire are highly associated
with older men who have died of heart failure.  In other words, the missing health scores were MNAR: the unobserved
health scores were exceedingly low (like "0" for no health at all).

It's weird, right?  One the one hand, it feels ok to call the missing data MAR... But the data are missing because
the heart health became so low that the patient ceased to exist, thus the data are missing based on the values
of the missing data........so MNAR, right?

## Graphical Models of Missingness

[Graphical Models for Inference with Missing Data](http://papers.nips.cc/paper/4899-graphical-models-for-inference-with-missing-data.pdf)

2015: [Missing Data as a Causal and Probabilistic Problem](https://apps.dtic.mil/dtic/tr/fulltext/u2/a623169.pdf)

2014: [On the Testability of Models with Missing Data](http://proceedings.mlr.press/v33/mohan14.pdf)

2014: [Graphical Models for Recovering Probabilistic and Causal Queries from Missing Data](https://papers.nips.cc/paper/5575-graphical-models-for-recovering-probabilistic-and-causal-queries-from-missing-data.pdf)

2015: [Graphical Representation of Missing Data Problems](https://ftp.cs.ucla.edu/pub/stat_ser/r448-reprint.pdf)

2018: [Graphical Models for Processing Missing Data](https://arxiv.org/pdf/1801.03583.pdf)

## Predictive Models in Practice

* [Prediction and Inference with Missing Data in Patient Alert Systems](https://arxiv.org/abs/1704.07904)

* [Prediction vs. Causation in Regression Analysis](https://statisticalhorizons.com/prediction-vs-causation-in-regression-analysis)

* [Effects of Different Missing Data Imputation Techniques on the Performance of Undiagnosed Diabetes Risk Prediction Models in a Mixed-Ancestry Population of South Africa](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0139210)

* [Missing data and prediction: the pattern submodel](https://academic.oup.com/biostatistics/advance-article/doi/10.1093/biostatistics/kxy040/5092384)

* [Methods for Handling Missing Variables in Risk Prediction Models](https://academic.oup.com/aje/article/184/7/545/2594506)

* [Obtaining Predictions from Models Fit to Multiply Imputed Data](https://journals.sagepub.com/doi/abs/10.1177/0049124115610345)
  - note2self: this one is not freely available online, but I have a copy in my email


## More General Missing Data Stuff

* [Multiple Imputation for General Missing Data Patterns in the Presence of High-dimensional Data](https://www.nature.com/articles/srep21689)
* [Multiple Imputation for Missing Data via Sequential Regression Trees](https://academic.oup.com/aje/article/172/9/1070/148540)
* [What to Do about Missing Values in Time-Series Cross-Section Data](https://dash.harvard.edu/bitstream/handle/1/4100248/Honaker_MissingValues.pdf?sequence=2&isAllowed=y)
* [Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls](https://www.bmj.com/content/338/bmj.b2393)
* [Missing Data Analysis Using Multiple Imputation: Getting to the Heart of the Matter](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2818781/)
* [Avoiding bias due to perfect prediction in multiple imputation of incomplete categorical variables](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3990447/)

## Historical Provenance

- Historical note: Curated in 2026 from draft notes originally committed in `krbnite.github.io` from 2018-12-19 to 2019-11-13. The source draft histories were imported into this repository before this consolidation step.
- Curation note: Consolidates causal-inference, missing-data, feature-type, and live-prediction draft notes.

### Source Drafts

- `causal-inference.md`
- `2019-03-28-Predictive-Models-for-Counterfactuals.md`
- `2019-04-01-Cat-Vars-and-Models-Take-2.md`
- `2019-04-05-Reflections-on-Feature-Types.md`
- `2019-04-19-Classifying-Circumstances-of-Missing-Data.md`
- `2019-04-19-Graphical-Models-of-Missingness.md`
- `predictive-models-in-practice.md`

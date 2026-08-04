# Time Series Forecasting and DSP Notes

> Historical provenance and source draft details are at [Historical Provenance](#historical-provenance).

## Machine Learning for Time Series Forecasting (2019-09-26; source: `2019-09-26-Machine-Learning-for-Time-Series-Forecasting.md`)

There's AR, MA, ARMA, ARIM, FARIMA, ARCH, GARCH, and more (didn't even being to list nonparametric
approaches).  These things stem from statistics, econometrics, and digital signal processing.  How and
where does ML come in for time series forecasting?  Obviously there are RNNs.  But what else?  RFs
basically suck at time series forecasting, at least if you're naive about it (they are great interpolators,
but terrible extrapolaters, so if you have a linear trend that continues past the historical/training
data, you're basically screwed -- at least without lots of pre- and post-processing external to the RF
itself).

So what else is there?

2012: Bontempi et al: [Machine learning strategies for time series forecasting](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C33&q=Machine+Learning+Strategies+for+Time+Series+Forecasting&btnG=)

## DSP in Python (2019-09-27; source: `2019-09-27-DSP-in-Python.md`)

http://ataspinar.com/2018/04/04/machine-learning-with-signal-processing-techniques/

https://www.datasciencecentral.com/profiles/blogs/a-guid-for-using-the-wavelet-transform-in-machine-learning

## Historical Provenance

- Historical note: Curated in 2026 from draft notes originally committed in `krbnite.github.io` from 2019-09-26 to 2019-09-27. The source draft histories were imported into this repository before this consolidation step.
- Curation note: Combines a short time-series modeling reflection with DSP-in-Python references.

### Source Drafts

- `2019-09-26-Machine-Learning-for-Time-Series-Forecasting.md`
- `2019-09-27-DSP-in-Python.md`

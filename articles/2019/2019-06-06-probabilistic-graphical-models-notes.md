# Probabilistic Graphical Models Notes

> Historical provenance and source draft details are at [Historical Provenance](#historical-provenance).

## Notes

[Introduction and Overview](https://www.coursera.org/lecture/probabilistic-graphical-models/welcome-7ri4Z)

* a model is a declarative representation of our understanding of the world
* probilistic represents uncertain, noisy, and/or partial knowledge of the world
  - probabilistic models provide declarative representation w/ clear semantics
  - powerful reasoning patterns (conditioning, stratifying, decision making)
  - established learning patterns
* graphical: computer science representation of complex system

Two main classes of PGM:
* Bayesian Network: directed graph that represents a joint probability distribution, where
  random variables are represented by nodes in the graph and edges represent the probabilistic connections
  between the RVs
* Markov Model: undirected graph where nodes are RVs
  - example: image segmentation

The graphical representation provides an intuitive and compact data structure that supports
general-purpose algorithms for efficient reasoning.

Applications include:
* medical diagnosis
* image segmentation
* robot path planning
* textual information extraction
* multi-sensor integration (data fusion)
* biological network reconstruction

Inference = reasoning...

--------------------------


Stanford's Course Notes: https://ermongroup.github.io/cs228-notes/

2013: Pearl: [Graphical Models for Probabilistic and Causal Reasoning](https://ftp.cs.ucla.edu/pub/stat_ser/r236-3ed.pdf)

Koller's textbook:  https://github.com/Zhenye-Na/machine-learning-uiuc/blob/master/docs/Probabilistic%20Graphical%20Models%20-%20Principles%20and%20Techniques.pdf


----------------------

For my sanity: [textbook](file:///Users/kevinurban/Downloads/Probabilistic%20Graphical%20Models%20-%20Principles%20and%20Techniques.pdf)

## Historical Provenance

- Historical note: Curated in 2026 from draft notes originally committed in `krbnite.github.io` from 2019-06-06 to 2019-06-07. The source draft histories were imported into this repository before this consolidation step.
- Curation note: A short probabilistic graphical models course-note fragment.

### Source Drafts

- `pgm1.md`

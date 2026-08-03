# Udacity AI for IoT Developers Nanodegree

Historical archive of a 2020 edge-AI / IoT learning project, centered on
Udacity's OpenVINO people-counter assignment.

The interesting parts of this repo are the setup notes, debugging notes, model
conversion logs, and small scripts around TensorFlow object-detection models,
OpenVINO Intermediate Representation conversion, FFMPEG, MQTT, and an Intel
Neural Compute Stick / Raspberry Pi style deployment path.

## Dates

The preserved Git history for this work runs from May 26, 2020 through July 15,
2020. This archive is kept as historical learning evidence rather than as a
freshly modernized implementation.

## What To Read

- `p01_people-counter/JOURNAL.md`: setup notes, environment pain, model
  selection, OpenVINO conversion attempts, and hardware/deployment debugging.
- `p01_people-counter/notes/object-detection.md`: personal notes on object
  detection concepts.
- `p01_people-counter/notes/myriad-issues.md`: notes on Intel NCS2 / MYRIAD
  troubleshooting.
- `p01_people-counter/src/models/`: helper scripts for downloading TensorFlow
  models and converting them to OpenVINO IR files.
- `p01_people-counter/logs/`: saved conversion/model-size notes from the 2020
  experiments.

## Large Files

Generated OpenVINO and TensorFlow model artifacts are intentionally excluded
from the preserved working tree. The original model outputs were large binary
files and are better treated as reproducible artifacts from the scripts and
notes, not as source files to keep in Git.

The small sample video is retained because it keeps the original project context
without making the archive large.

## Status

This should be read as a preserved course-era project and notebook-adjacent
learning record. The project contains starter-code scaffolding from the Udacity
assignment plus personal notes and experiments; it is not presented as a
completed production people-counter application.

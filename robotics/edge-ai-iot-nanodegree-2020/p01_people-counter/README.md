# People Counter at the Edge

This directory preserves my 2020 work around Udacity's AI for IoT Developers
Nanodegree people-counter project. The assignment was to detect people in a
video stream, count how many were in frame, estimate how long each person stayed
in frame, and send the results through a small MQTT / FFMPEG / web UI pipeline.

The original course README is preserved separately in
`UDACITY_ORIGINAL_README.md`. This file is the shorter map of what I was doing
and what is worth reading now.

## My Angle

The Udacity workspace provided a ready-made environment, but I was trying to
understand what it took to run the project locally and closer to real edge
hardware. At the time I had bought a CanaKit Raspberry Pi 4B kit and planned to
use it alongside an Intel Neural Compute Stick 2.

That led to most of the interesting work in this folder: environment notes,
OpenVINO setup, TensorFlow model conversion, FFMPEG and Node server setup, and
MYRIAD/NCS2 debugging.

## What To Read

- `JOURNAL.md`: the main working log, including setup notes, model selection,
  OpenVINO conversion attempts, and local runtime debugging.
- `notes/object-detection.md`: conceptual notes on object-detection models and
  detection pipelines.
- `notes/myriad-issues.md`: notes from trying to reason through NCS2 / MYRIAD
  runtime problems.
- `src/models/`: shell helpers for downloading TensorFlow Object Detection Model
  Zoo models and converting them to OpenVINO IR artifacts.
- `logs/`: saved model conversion and size-comparison outputs.

## Broad Strokes Of The Assignment

- Use a model that can detect people in video frames.
- Convert that model to OpenVINO Intermediate Representation format.
- Run inference through OpenVINO's Inference Engine.
- Publish people-counting stats to an MQTT server.
- Stream processed frames through FFMPEG to a browser UI.
- Support CPU inference and, ideally, Intel Neural Compute Stick / MYRIAD
  inference with FP16 models.

## Preserved Course Material

The original assignment README is kept in `UDACITY_ORIGINAL_README.md` for
context. It includes the Udacity setup instructions, architecture diagram, run
commands, and notes about CPU versus Neural Compute Stick execution.

Generated model files are intentionally omitted from this archive. They were
large OpenVINO/TensorFlow artifacts produced by the scripts and notes, not source
files that need to live in Git.

## Historical Status

This archive is not a polished final implementation. My original goal was to run
the people-counter project locally and eventually test it on a Raspberry Pi with
an Intel Neural Compute Stick 2, but the course-era tooling was fragile and time
constraints made the supported Udacity environment the practical path for
finishing the class.

Some of the setup, debugging, model-selection, and OpenVINO conversion work is
captured here, especially in `JOURNAL.md`, but not every experiment made it into
Git. This folder is preserved as evidence of the 2020 learning process around
edge AI deployment rather than as a complete production-ready application.
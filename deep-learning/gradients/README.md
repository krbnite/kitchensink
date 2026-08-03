# Gradient Inspection Notes

This mini-project preserves some notes from 2020 about inspecting neural-network 
gradients in TensorFlow 2.2. It then re-implements these ideas using modern (2026) TensorFlow and 
PyTorch.

The original note lives in `original-2020-gradients.md`. It is intentionally kept close to the source material: it has the feel of 2020 TensorFlow, where `tf.compat.v1`, disabled eager execution, Keras backend functions, and sessions could still be part of a normal debugging path.

## Files

- `original-2020-gradients.md`: preserved source note from the old notes folder.
- `gradients-2020-tf22-compat.ipynb`: cleaned notebook version of the 2020 TensorFlow/Keras backend approach.
- `gradients-modern-tf-pytorch.ipynb`: modern companion notebook using `tf.GradientTape` and `torch.autograd`.
- `gradients-env.sh`: local Conda environment helper.
- `.gitignore`: keeps local Conda envs, caches, logs, and generated scratch output out of git.

## Environment Setup

First make the script executable:

```bash
chmod +x gradients-env.sh
```

For the historical TensorFlow 2.2 environment:

```bash
./gradients-env.sh legacy2020
conda activate ./.conda-gradients-2020
jupyter lab gradients-2020-tf22-compat.ipynb
```

For the modern environment:

```bash
./gradients-env.sh modern
conda activate ./.conda-gradients-modern
jupyter lab gradients-modern-tf-pytorch.ipynb
```

The legacy environment uses Python 3.8 and TensorFlow 2.2.0 because TensorFlow 2.2.0 was released in May 2020 and supported Python 3.5-3.8 on PyPI. On Apple Silicon Macs, this may require an x86_64/Rosetta environment, Docker, or Colab because TensorFlow 2.2 predates native Apple Silicon wheels.

The modern environment pins TensorFlow 2.21.0 and PyTorch 2.13.0 as the current reference versions at the time this note was refreshed. TensorFlow 2.21 requires Python 3.10 or newer, and PyTorch 2.13 also requires Python 3.10 or newer.

## Why Two Notebooks?

The 2020 code disables TensorFlow eager execution and uses static graph/session habits. That is valuable historically, but it changes global TensorFlow runtime behavior and is not compatible in the same Python environment with modern TensorFlow and PyTorch. So the 2020 notebook is preserved in its own environment, and the modern notebook is run in a separate environment.

The modern notebook uses the two APIs that are most common today for inspecting gradients:

- TensorFlow: `tf.GradientTape`
- PyTorch: `torch.autograd`


## Main Lesson

The old notebook asks, "How do I reach into this Keras graph and get the gradients I want?"

The modern notebook asks, "What tensors did my forward pass produce, and which of them should my autodiff tape remember?"

Both notebooks show how to inspect gradients with respect to trainable weights and intermediate activations. 


## References

- TensorFlow autodiff guide: https://www.tensorflow.org/guide/autodiff
- TensorFlow custom training loop guide: https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch
- TensorFlow pip install guide: https://www.tensorflow.org/install/pip
- TensorFlow 2.2.0 on PyPI: https://pypi.org/project/tensorflow/2.2.0/
- PyTorch autograd docs: https://docs.pytorch.org/docs/main/autograd.html
- PyTorch on PyPI: https://pypi.org/project/torch/

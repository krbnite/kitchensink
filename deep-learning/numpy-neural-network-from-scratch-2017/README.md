# NumPy Neural Network From Scratch

Standalone mini-project based on 2017 course work around deriving and
implementing neural networks from first principles.

## What It Shows

- A fully connected neural network implemented with NumPy.
- Forward propagation through affine, ReLU, and sigmoid layers.
- Binary cross-entropy loss.
- Backpropagation for each layer.
- Parameter updates with gradient descent.
- A finite-difference gradient check.
- Training on a generated two-moons classification dataset.

## Files

- `numpy-neural-network-from-scratch.ipynb`: standalone notebook.
- `nn-from-scratch-env.sh`: optional Conda environment helper.
- `.gitignore`: keeps local environments, notebook checkpoints, and caches out
  of Git.

## Environment

First make the script executable:

```bash
chmod +x nn-from-scratch-env.sh
```

Then create and activate the local environment:

```bash
./nn-from-scratch-env.sh
conda activate ./.conda-nn-scratch
jupyter lab numpy-neural-network-from-scratch.ipynb
```

The notebook only needs NumPy to run the neural-network code. Matplotlib is used
for optional plots.

## Historical Note

The original private notebooks were part of my 2017 deep-learning study path,
when I was working through neural-network notation, vectorized matrix
implementations, and backpropagation by hand. This public reconstruction keeps
that learning goal while avoiding publication of non-public scaffolding or
private exercise material.

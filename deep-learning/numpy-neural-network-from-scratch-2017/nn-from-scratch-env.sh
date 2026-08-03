#!/usr/bin/env bash
set -euo pipefail

# Build a small local Conda environment for the standalone NumPy notebook.
# The environment lives inside this folder and is ignored by Git.
ENV_DIR=".conda-nn-scratch"

if ! command -v conda >/dev/null 2>&1; then
  echo "conda was not found. Install Miniconda or Anaconda first."
  exit 1
fi

if [ ! -d "$ENV_DIR" ]; then
  conda create -y -p "$ENV_DIR" python=3.11 numpy matplotlib jupyterlab
else
  echo "Environment already exists at $ENV_DIR"
fi

echo
echo "Activate with:"
echo "  conda activate ./$ENV_DIR"

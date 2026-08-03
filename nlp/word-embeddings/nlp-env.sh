#!/usr/bin/env bash
set -euo pipefail

# Build a small local Conda environment for the word-embeddings note and demo.
# The environment lives inside this folder and is ignored by git.

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_DIR="${PROJECT_DIR}/.conda-word-embeddings"
NLTK_DATA_DIR="${PROJECT_DIR}/nltk_data"

usage() {
  cat <<'USAGE'
Usage:
  ./nlp-env.sh

After install:
  conda activate ./.conda-word-embeddings
  jupyter lab word-embeddings-demo.ipynb
USAGE
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ] || [ "${1:-}" = "help" ]; then
  usage
  exit 0
fi

if ! command -v conda >/dev/null 2>&1; then
  echo "Could not find conda. Install Miniconda or Anaconda first."
  exit 1
fi

# Make `conda activate` work from this non-interactive script.
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"

if [ ! -d "${ENV_DIR}" ]; then
  conda create -y -p "${ENV_DIR}" "python=3.11"
fi

conda activate "${ENV_DIR}"

python -m pip install --upgrade pip setuptools wheel
python -m pip install \
  "numpy<3" \
  nltk \
  scikit-learn \
  matplotlib \
  jupyterlab \
  ipykernel

mkdir -p "${NLTK_DATA_DIR}"
export NLTK_DATA="${NLTK_DATA_DIR}"

python - <<'PY'
import os
import nltk

download_dir = os.environ["NLTK_DATA"]
nltk.download("wordnet", download_dir=download_dir, quiet=True)
nltk.download("omw-1.4", download_dir=download_dir, quiet=True)
PY

python -m ipykernel install \
  --user \
  --name "word-embeddings" \
  --display-name "Python (word embeddings)"

python -m pip check

#!/usr/bin/env bash
set -euo pipefail

# Build a local Conda environment for either the historical 2020 notebook or
# the modern TensorFlow/PyTorch companion notebook. The environments live in
# this folder so the mini-project stays self-contained inside kitchensink.

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LEGACY_ENV_DIR="${PROJECT_DIR}/.conda-gradients-2020"
MODERN_ENV_DIR="${PROJECT_DIR}/.conda-gradients-modern"

usage() {
  cat <<'USAGE'
Usage:
  ./gradients-env.sh legacy2020
  ./gradients-env.sh modern

Modes:
  legacy2020  Python 3.8 + TensorFlow 2.2.0 for the compatibility notebook.
  modern      Python 3.11 + current TensorFlow/PyTorch gradient APIs.

After install:
  conda activate ./.conda-gradients-2020
  conda activate ./.conda-gradients-modern
USAGE
}

require_conda() {
  if ! command -v conda >/dev/null 2>&1; then
    echo "Could not find conda. Install Miniconda or Anaconda first."
    exit 1
  fi

  # Make `conda activate` work from this non-interactive script.
  # shellcheck disable=SC1091
  source "$(conda info --base)/etc/profile.d/conda.sh"
}

create_env_if_needed() {
  local env_dir="$1"
  local python_version="$2"

  if [ ! -d "${env_dir}" ]; then
    conda create -y -p "${env_dir}" "python=${python_version}"
  fi
}

install_kernel() {
  local kernel_name="$1"
  local display_name="$2"

  python -m ipykernel install \
    --user \
    --name "${kernel_name}" \
    --display-name "${display_name}"
}

install_legacy2020() {
  require_conda

  if [ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ]; then
    cat <<'NOTE'
Warning:
  TensorFlow 2.2.0 predates native Apple Silicon wheels. This install may fail
  on arm64 Macs unless the terminal/Conda stack is running under x86_64/Rosetta.
  The notebook is still useful as a preserved 2020 reference even if you run it
  in Colab, Docker, or an older Intel-compatible environment.
NOTE
  fi

  create_env_if_needed "${LEGACY_ENV_DIR}" "3.8"
  conda activate "${LEGACY_ENV_DIR}"

  # Older scientific Python packages are more cooperative with an older pip.
  python -m pip install --upgrade "pip<24" setuptools wheel
  python -m pip install \
    "numpy==1.18.5" \
    "tensorflow==2.2.0" \
    "matplotlib==3.3.4" \
    "scikit-learn==0.23.2" \
    "notebook<7" \
    "jupyterlab<4" \
    "ipykernel<7"

  install_kernel "gradients-2020" "Python (gradients 2020)"
  python -m pip check
}

install_modern() {
  require_conda
  create_env_if_needed "${MODERN_ENV_DIR}" "3.11"
  conda activate "${MODERN_ENV_DIR}"

  python -m pip install --upgrade pip setuptools wheel
  python -m pip install \
    "tensorflow==2.21.0" \
    "torch==2.13.0" \
    "numpy<3" \
    matplotlib \
    scikit-learn \
    jupyterlab \
    ipykernel

  install_kernel "gradients-modern" "Python (gradients modern)"
  python -m pip check
}

case "${1:-}" in
  legacy2020)
    install_legacy2020
    ;;
  modern)
    install_modern
    ;;
  -h|--help|help|"")
    usage
    ;;
  *)
    echo "Unknown mode: $1"
    usage
    exit 1
    ;;
esac

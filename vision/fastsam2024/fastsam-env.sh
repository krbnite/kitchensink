#!/usr/bin/env bash
set -euo pipefail

# The notebook has two paths:
# - ultralytics: the main flow using `from ultralytics import FastSAM`
# - casia: the later flow using the local CASIA FastSAM clone in ./FastSAM
MODE=""
RESET=0
ENV_ROOT=""
PYTHON_VERSION="3.12"
FASTSAM_REPO_URL="https://github.com/CASIA-IVA-Lab/FastSAM.git"
FASTSAM_COMMIT="b4ed20c2fed75eadc5aa7d8b09fedd137b873b52"

usage() {
  printf '%s\n' "Usage: ./fastsam-env.sh [ultralytics|casia] [--reset] [--env-root PATH]"
  printf '%s\n' ""
  printf '%s\n' "Examples:"
  printf '%s\n' "  ./fastsam-env.sh ultralytics"
  printf '%s\n' "  ./fastsam-env.sh casia"
  printf '%s\n' "  ./fastsam-env.sh ultralytics --reset"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    ultralytics|ultra)
      MODE="ultralytics"
      shift
      ;;
    casia)
      MODE="casia"
      shift
      ;;
    --reset)
      RESET=1
      shift
      ;;
    --env-root)
      ENV_ROOT="${2:-}"
      if [ -z "$ENV_ROOT" ]; then
        printf '%s\n' "--env-root needs a path." >&2
        exit 2
      fi
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown option: %s\n' "$1" >&2
      usage
      exit 2
      ;;
  esac
done

if [ -z "$MODE" ]; then
  MODE="ultralytics"
fi

if ! command -v conda >/dev/null 2>&1; then
  printf '%s\n' "Conda was not found on PATH. Install Miniconda/Miniforge or initialize conda first." >&2
  exit 1
fi

if [ -z "$ENV_ROOT" ]; then
  # Keep environments project-local so deleting this folder cleans them up too.
  ENV_ROOT="$PWD/.conda-fastsam-$MODE"
fi

CONDA_BASE="$(conda info --base)"
# shellcheck disable=SC1091
source "$CONDA_BASE/etc/profile.d/conda.sh"

if [ "$RESET" -eq 1 ] && [ -d "$ENV_ROOT" ]; then
  rm -rf "$ENV_ROOT"
fi

install_torch() {
  case "$(uname -s)" in
    Darwin)
      # macOS wheels include Apple Silicon/MPS support where available.
      python -m pip install "torch" "torchvision"
      ;;
    *)
      # Use CPU wheels by default so this setup works without a CUDA install.
      python -m pip install "torch" "torchvision" --index-url https://download.pytorch.org/whl/cpu
      ;;
  esac
}

install_common_notebook_packages() {
  python -m pip install --upgrade pip
  python -m pip install \
    "jupyter" \
    "ipykernel" \
    "pandas" \
    "seaborn" \
    "matplotlib" \
    "pillow" \
    "numpy"
}

install_ultralytics_packages() {
  install_common_notebook_packages
  install_torch
  python -m pip install "ultralytics==8.2.65"
  python -m pip install "git+https://github.com/openai/CLIP.git"
  python -m pip check
}

install_casia_packages() {
  install_common_notebook_packages
  install_torch
  python -m pip install \
    "opencv-python>=4.6.0" \
    "PyYAML>=5.3.1" \
    "requests>=2.23.0" \
    "scipy>=1.4.1" \
    "tqdm>=4.64.0"
  python -m pip install "git+https://github.com/openai/CLIP.git"
  python -m pip check
}

ensure_casia_fastsam_clone() {
  if [ ! -d "FastSAM/.git" ]; then
    rm -rf "FastSAM"
    git clone "$FASTSAM_REPO_URL" FastSAM
  fi

  git -C FastSAM checkout --force "$FASTSAM_COMMIT"

  # The notebook's CASIA text-prompt path needs CLIP imported in prompt.py.
  python - <<'PY'
from pathlib import Path

path = Path("FastSAM/fastsam/prompt.py")
text = path.read_text()
if "import clip\n" not in text:
    lines = text.splitlines(keepends=True)
    insert_at = 0
    for index, line in enumerate(lines):
        if line.startswith("import ") or line.startswith("from "):
            insert_at = index + 1
    lines.insert(insert_at, "import clip\n")
    path.write_text("".join(lines))
PY
}

if [ ! -d "$ENV_ROOT" ]; then
  conda create -y -p "$ENV_ROOT" "python=$PYTHON_VERSION" pip
  conda activate "$ENV_ROOT"
  printf '%s\n' "$MODE" > "$ENV_ROOT/.fastsam-env-kind"

  if [ "$MODE" = "ultralytics" ]; then
    install_ultralytics_packages
  else
    ensure_casia_fastsam_clone
    install_casia_packages
  fi
else
  conda activate "$ENV_ROOT"
  if [ "$MODE" = "casia" ]; then
    ensure_casia_fastsam_clone
  fi
fi

export FASTSAM_ENV_KIND="$MODE"
export FASTSAM_ENV_ROOT="$ENV_ROOT"

printf '\nActivated FastSAM %s environment:\n  %s\n\n' "$MODE" "$CONDA_PREFIX"
printf '%s\n' "Try:"
printf '%s\n' "  jupyter lab fastsam.ipynb"
printf '%s\n' "  jupyter notebook fastsam.ipynb"
printf '\n'

exec "${SHELL:-/bin/bash}" -i

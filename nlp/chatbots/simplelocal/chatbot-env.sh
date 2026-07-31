#!/usr/bin/env bash
set -euo pipefail

# MODE chooses the dependency stack. By default, use the newer stack because it
# handles more current Hugging Face models.
MODE=""
RESET=0
ENV_ROOT=""
PYTHON_VERSION="3.11"

usage() {
  printf '%s\n' "Usage: ./chatbot-env.sh [course|modern] [--reset] [--env-root PATH]"
  printf '%s\n' ""
  printf '%s\n' "Examples:"
  printf '%s\n' "  ./chatbot-env.sh course"
  printf '%s\n' "  ./chatbot-env.sh modern"
  printf '%s\n' "  ./chatbot-env.sh modern --reset"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    course|old)
      MODE="course"
      shift
      ;;
    modern|new)
      MODE="modern"
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
  MODE="modern"
fi

if ! command -v conda >/dev/null 2>&1; then
  printf '%s\n' "Conda was not found on PATH. Install Miniconda/Miniforge or initialize conda first." >&2
  exit 1
fi

if [ -z "$ENV_ROOT" ]; then
  # Keep environments project-local so this folder can be copied or deleted
  # without touching global Conda environments.
  ENV_ROOT="$PWD/.conda-chatbot-$MODE"
fi

CONDA_BASE="$(conda info --base)"
# Load Conda's shell helpers so this script can activate an env reliably.
# shellcheck disable=SC1091
source "$CONDA_BASE/etc/profile.d/conda.sh"

if [ "$RESET" -eq 1 ] && [ -d "$ENV_ROOT" ]; then
  # This only removes the local chatbot env path selected above.
  rm -rf "$ENV_ROOT"
fi

install_pytorch_course() {
  case "$(uname -s)" in
    Darwin)
      # PyTorch's macOS wheels do not use the +cpu suffix.
      python -m pip install \
        "torch==2.2.2" \
        "torchvision==0.17.2" \
        "torchaudio==2.2.2" \
        "torchtext==0.17.2"
      ;;
    *)
      # Linux/Windows CPU wheels live on the PyTorch index and use +cpu names.
      python -m pip install \
        "torch==2.2.2+cpu" \
        "torchvision==0.17.2+cpu" \
        "torchaudio==2.2.2+cpu" \
        "torchtext==0.17.2+cpu" \
        --index-url https://download.pytorch.org/whl/cpu
      ;;
  esac
}

install_pytorch_modern() {
  case "$(uname -s)" in
    Darwin)
      # Current macOS wheels include Apple Silicon support where available.
      python -m pip install -U torch
      ;;
    *)
      python -m pip install -U torch --index-url https://download.pytorch.org/whl/cpu
      ;;
  esac
}

install_course_packages() {
  python -m pip install --upgrade pip
  python -m pip install \
    "numpy==1.26.4" \
    "scipy==1.13.1" \
    "scikit-learn==1.5.0" \
    "nltk" \
    "transformers==4.42.1" \
    "sentencepiece" \
    "spacy"
  install_pytorch_course
  python -m pip check
}

install_modern_packages() {
  python -m pip install --upgrade pip
  install_pytorch_modern
  python -m pip install -U \
    "transformers>=4.51.0" \
    "tokenizers>=0.21.0" \
    "accelerate" \
    "safetensors" \
    "sentencepiece"
  python -m pip check
}

if [ ! -d "$ENV_ROOT" ]; then
  conda create -y -p "$ENV_ROOT" "python=$PYTHON_VERSION" pip
  conda activate "$ENV_ROOT"
  # chatbot.py reads this marker when recommending models.
  printf '%s\n' "$MODE" > "$ENV_ROOT/.chatbot-env-kind"

  if [ "$MODE" = "course" ]; then
    install_course_packages
  else
    install_modern_packages
  fi
else
  conda activate "$ENV_ROOT"
fi

# Export these for the current shell that opens after activation.
export CHATBOT_ENV_KIND="$MODE"
export CHATBOT_ENV_ROOT="$ENV_ROOT"

printf '\nActivated chatbot %s environment:\n  %s\n\n' "$MODE" "$CONDA_PREFIX"
printf '%s\n' "Try:"
printf '%s\n' "  python chatbot.py --recommend-models"
printf '%s\n' "  python chatbot.py --model qwen2-0.5b"
if [ "$MODE" = "modern" ]; then
  printf '%s\n' "  python chatbot.py --model qwen3-4b"
fi
printf '\n'

# Replace this process with an interactive shell so the user stays inside the
# activated environment after the setup work finishes.
exec "${SHELL:-/bin/bash}" -i

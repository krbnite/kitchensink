#!/usr/bin/env python3
import argparse
import importlib.util
import os
import platform
import shutil
import subprocess
import sys

import torch
import transformers
from packaging.version import Version
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
)


# Presets keep the command line friendly while still allowing a raw Hugging Face
# model id through --model. The RAM/disk numbers are practical guardrails, not
# exact model requirements.
MODEL_PRESETS = {
    "qwen2-0.5b": {
        "id": "Qwen/Qwen2-0.5B-Instruct",
        "label": "Good default for the course environment; small instruct model.",
        "min_transformers": "4.37.0",
        "envs": {"course", "modern"},
        "min_ram_gb": 8,
        "recommended_ram_gb": 16,
        "min_disk_gb": 3,
    },
    "qwen2.5-0.5b": {
        "id": "Qwen/Qwen2.5-0.5B-Instruct",
        "label": "Slightly newer small instruct model; should fit transformers 4.42.1.",
        "min_transformers": "4.37.0",
        "envs": {"course", "modern"},
        "min_ram_gb": 8,
        "recommended_ram_gb": 16,
        "min_disk_gb": 3,
    },
    "smollm2-135m": {
        "id": "HuggingFaceTB/SmolLM2-135M-Instruct",
        "label": "Tiny and fast, but less capable.",
        "envs": {"course", "modern"},
        "min_ram_gb": 4,
        "recommended_ram_gb": 8,
        "min_disk_gb": 2,
    },
    "smollm2-360m": {
        "id": "HuggingFaceTB/SmolLM2-360M-Instruct",
        "label": "Small, English-focused instruct model.",
        "envs": {"course", "modern"},
        "min_ram_gb": 6,
        "recommended_ram_gb": 12,
        "min_disk_gb": 3,
    },
    "tinyllama-1.1b": {
        "id": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "label": "Bigger and slower on CPU, but a familiar chat baseline.",
        "min_transformers": "4.34.0",
        "envs": {"course", "modern"},
        "min_ram_gb": 12,
        "recommended_ram_gb": 24,
        "min_disk_gb": 5,
    },
    "blenderbot-400m": {
        "id": "facebook/blenderbot-400M-distill",
        "label": "Classic seq2seq chatbot; no chat template, simple current-turn replies.",
        "envs": {"course", "modern"},
        "min_ram_gb": 6,
        "recommended_ram_gb": 12,
        "min_disk_gb": 3,
    },
    "qwen3-4b": {
        "id": "Qwen/Qwen3-4B-Instruct-2507",
        "label": "For your bigger-model environment, not transformers 4.42.1.",
        "min_transformers": "4.51.0",
        "envs": {"modern"},
        "min_ram_gb": 24,
        "recommended_ram_gb": 32,
        "min_disk_gb": 12,
    },
}


SYSTEM_PROMPT = "You are a helpful, concise chatbot."
EXIT_WORDS = {"quit", "exit", "bye"}
MODEL_WEIGHT_SUFFIXES = (".safetensors", ".bin")


def parse_args():
    parser = argparse.ArgumentParser(description="Small reusable local chatbot.")
    parser.add_argument(
        "--model",
        default="qwen2-0.5b",
        help="Preset name or Hugging Face model id. Use --list-models to see presets.",
    )
    parser.add_argument("--list-models", action="store_true")
    parser.add_argument(
        "--recommend-models",
        action="store_true",
        help="Inspect this environment and machine, then print practical model choices.",
    )
    parser.add_argument("--system", default=SYSTEM_PROMPT)
    parser.add_argument("--max-new-tokens", type=int, default=120)
    parser.add_argument("--max-context-tokens", type=int, default=1536)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--no-sample", action="store_true")
    parser.add_argument(
        "--no-device-map",
        action="store_true",
        help="Disable accelerate device_map='auto' even when accelerate is installed.",
    )
    parser.add_argument(
        "--allow-heavy",
        action="store_true",
        help="Override RAM/disk preflight checks for large or unknown models.",
    )
    return parser.parse_args()


def list_models():
    width = max(len(name) for name in MODEL_PRESETS)
    for name, preset in MODEL_PRESETS.items():
        print(f"{name:<{width}}  {preset['id']}")
        print(f"{'':<{width}}  {preset['label']}")


def resolve_model(name_or_id):
    preset = MODEL_PRESETS.get(name_or_id)
    if preset is None:
        for candidate in MODEL_PRESETS.values():
            if candidate["id"] == name_or_id:
                return name_or_id, candidate
        return name_or_id, {}
    return preset["id"], preset


def require_transformers_version(preset):
    minimum = preset.get("min_transformers")
    if not minimum:
        return
    current = Version(transformers.__version__)
    required = Version(minimum)
    if current < required:
        raise SystemExit(
            f"This model needs transformers>={minimum}, but this environment has "
            f"transformers=={transformers.__version__}."
        )


def bytes_to_gb(value):
    if value is None:
        return None
    return value / (1024**3)


def format_gb(value):
    if value is None:
        return "unknown"
    return f"{value:.1f} GB"


def existing_parent(path):
    path = os.path.abspath(os.path.expanduser(path))
    while not os.path.exists(path):
        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent
    return path


def huggingface_cache_path():
    # Hugging Face usually downloads weights into its cache, not necessarily the
    # current project folder.
    if os.environ.get("HF_HUB_CACHE"):
        return os.environ["HF_HUB_CACHE"]
    if os.environ.get("TRANSFORMERS_CACHE"):
        return os.environ["TRANSFORMERS_CACHE"]
    if os.environ.get("HF_HOME"):
        return os.path.join(os.environ["HF_HOME"], "hub")
    return os.path.expanduser("~/.cache/huggingface/hub")


def total_memory_bytes():
    system = platform.system()
    if system == "Darwin":
        try:
            # macOS does not expose /proc/meminfo, so ask the kernel directly.
            result = subprocess.run(
                ["sysctl", "-n", "hw.memsize"],
                capture_output=True,
                check=True,
                text=True,
            )
            return int(result.stdout.strip())
        except (OSError, subprocess.CalledProcessError, ValueError):
            return None

    if system == "Linux":
        try:
            # Linux reports memory in KiB in /proc/meminfo.
            with open("/proc/meminfo", "r", encoding="utf-8") as handle:
                for line in handle:
                    if line.startswith("MemTotal:"):
                        return int(line.split()[1]) * 1024
        except OSError:
            return None

    if system == "Windows":
        try:
            import ctypes

            # GlobalMemoryStatusEx is available without installing psutil.
            class MemoryStatus(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            status = MemoryStatus()
            status.dwLength = ctypes.sizeof(status)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
            return int(status.ullTotalPhys)
        except (AttributeError, OSError, ValueError):
            return None

    if hasattr(os, "sysconf"):
        try:
            pages = os.sysconf("SC_PHYS_PAGES")
            page_size = os.sysconf("SC_PAGE_SIZE")
            return int(pages * page_size)
        except (OSError, ValueError):
            return None
    return None


def gpu_memory_bytes():
    if torch.cuda.is_available():
        return torch.cuda.get_device_properties(0).total_memory
    return None


def detect_env_kind():
    # chatbot-env.sh exports this; the marker file lets a new shell recover the
    # same answer after activation.
    env_kind = os.environ.get("CHATBOT_ENV_KIND")
    if env_kind in {"course", "modern"}:
        return env_kind

    conda_prefix = os.environ.get("CONDA_PREFIX")
    if conda_prefix:
        marker = os.path.join(conda_prefix, ".chatbot-env-kind")
        try:
            with open(marker, "r", encoding="utf-8") as handle:
                marker_value = handle.read().strip()
            if marker_value in {"course", "modern"}:
                return marker_value
        except OSError:
            pass

    # Last resort: infer from transformers. Qwen3-compatible environments need
    # a much newer release than the course stack.
    if Version(transformers.__version__) >= Version("4.51.0"):
        return "modern"
    return "course"


def system_profile():
    cache_path = huggingface_cache_path()
    disk = shutil.disk_usage(existing_parent(cache_path))
    device = preferred_device()
    return {
        "env_kind": detect_env_kind(),
        "python": platform.python_version(),
        "platform": f"{platform.system()} {platform.machine()}",
        "device": device,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "total_ram_gb": bytes_to_gb(total_memory_bytes()),
        "gpu_ram_gb": bytes_to_gb(gpu_memory_bytes()),
        "free_disk_gb": bytes_to_gb(disk.free),
        "cache_path": cache_path,
    }


def version_issue(preset):
    minimum = preset.get("min_transformers")
    if minimum and Version(transformers.__version__) < Version(minimum):
        return f"needs transformers>={minimum}"
    return None


def model_fit(profile, preset):
    # Split hard blockers from "works, but may feel slow" warnings so the output
    # can show clear recommendations without hiding borderline options.
    reasons = []
    warnings = []

    if profile["env_kind"] not in preset.get("envs", {"course", "modern"}):
        reasons.append(f"for {', '.join(sorted(preset['envs']))} env")

    issue = version_issue(preset)
    if issue:
        reasons.append(issue)

    total_ram_gb = profile["total_ram_gb"]
    if total_ram_gb is not None:
        if total_ram_gb < preset.get("min_ram_gb", 0):
            reasons.append(f"needs about {preset['min_ram_gb']} GB RAM")
        elif total_ram_gb < preset.get("recommended_ram_gb", 0):
            warnings.append("may be slow or tight on RAM")

    free_disk_gb = profile["free_disk_gb"]
    if free_disk_gb is not None and free_disk_gb < preset.get("min_disk_gb", 0):
        reasons.append(f"needs about {preset['min_disk_gb']} GB free disk")

    if preset.get("id", "").startswith("Qwen/Qwen3") and profile["device"] == "cpu":
        warnings.append("large for CPU-only use")

    return reasons, warnings


def sibling_size(sibling):
    size = getattr(sibling, "size", None)
    if size is not None:
        return size

    lfs = getattr(sibling, "lfs", None)
    if isinstance(lfs, dict):
        return lfs.get("size")
    return getattr(lfs, "size", None)


def weight_file_kind(filename):
    basename = os.path.basename(filename)
    if not basename.endswith(MODEL_WEIGHT_SUFFIXES):
        return None
    if basename.endswith(".index.json"):
        return None
    if basename.endswith(".safetensors"):
        return "safetensors"
    if basename.endswith(".bin"):
        return "bin"
    return None


def local_weight_estimate(path):
    weights = {"safetensors": [], "bin": []}
    if os.path.isfile(path):
        kind = weight_file_kind(path)
        if kind:
            weights[kind].append(os.path.getsize(path))
    else:
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(root, filename)
                kind = weight_file_kind(full_path)
                if kind:
                    weights[kind].append(os.path.getsize(full_path))

    selected = weights["safetensors"] or weights["bin"]
    if not selected:
        return None
    return {
        "bytes": sum(selected),
        "files": len(selected),
        "source": "local weight files",
    }


def hub_weight_estimate(model_id):
    try:
        from huggingface_hub import HfApi
    except ImportError:
        return None, "huggingface_hub is not installed"

    try:
        info = HfApi().model_info(model_id, files_metadata=True, timeout=10)
    except Exception as exc:
        return None, str(exc)

    weights = {"safetensors": [], "bin": []}
    for sibling in getattr(info, "siblings", []) or []:
        filename = getattr(sibling, "rfilename", "")
        kind = weight_file_kind(filename)
        size = sibling_size(sibling)
        if kind and size:
            weights[kind].append(size)

    selected = weights["safetensors"] or weights["bin"]
    if not selected:
        return None, "no PyTorch or safetensors weight metadata found"

    return {
        "bytes": sum(selected),
        "files": len(selected),
        "source": "Hugging Face Hub file metadata",
    }, None


def model_weight_estimate(model_id):
    local_path = os.path.expanduser(model_id)
    if os.path.exists(local_path):
        estimate = local_weight_estimate(local_path)
        if estimate:
            return estimate, None
        return None, "no local PyTorch or safetensors weight files found"

    if "/" not in model_id:
        return None, "not a local path or Hugging Face repo id"

    return hub_weight_estimate(model_id)


def estimated_requirements_from_weights(weight_bytes, profile):
    weight_gb = bytes_to_gb(weight_bytes)
    disk_needed_gb = max(2.0, weight_gb * 1.4)

    if profile["device"] == "cuda":
        ram_needed_gb = max(6.0, weight_gb * 1.4 + 2.0)
        gpu_needed_gb = max(2.0, weight_gb * 1.2)
    else:
        # CPU and Apple MPS both use system memory. Loading can briefly duplicate
        # model weights, so leave a generous margin.
        ram_needed_gb = max(6.0, weight_gb * 2.5 + 2.0)
        gpu_needed_gb = None

    return {
        "weight_gb": weight_gb,
        "disk_needed_gb": disk_needed_gb,
        "ram_needed_gb": ram_needed_gb,
        "gpu_needed_gb": gpu_needed_gb,
    }


def recommended_model_names(profile):
    names = []
    for name, preset in MODEL_PRESETS.items():
        reasons, warnings = model_fit(profile, preset)
        if not reasons and not warnings:
            names.append(name)
    return names


def stop_for_preflight(model_name, reasons, profile):
    print("Preflight stopped before downloading or loading model weights.")
    print()
    print(f"Requested model: {model_name}")
    print("Reasons:")
    for reason in reasons:
        print(f"  - {reason}")

    alternatives = recommended_model_names(profile)
    if alternatives:
        print()
        print("Try one of these instead:")
        for name in alternatives[:4]:
            print(f"  python chatbot.py --model {name}")

    print()
    print("To override this safety check, add --allow-heavy.")
    raise SystemExit(1)


def preflight_model(model_id, preset, args):
    profile = system_profile()
    reasons = []
    warnings = []

    if preset:
        preset_reasons, preset_warnings = model_fit(profile, preset)
        reasons.extend(preset_reasons)
        warnings.extend(preset_warnings)

    if not preset:
        estimate, error = model_weight_estimate(model_id)
        if error:
            reasons.append(f"could not check model size before download: {error}")
        else:
            requirements = estimated_requirements_from_weights(estimate["bytes"], profile)
            total_ram_gb = profile["total_ram_gb"]
            free_disk_gb = profile["free_disk_gb"]
            gpu_ram_gb = profile["gpu_ram_gb"]

            print(
                "Preflight estimate: "
                f"{format_gb(requirements['weight_gb'])} of model weights "
                f"across {estimate['files']} file(s) from {estimate['source']}."
            )

            if total_ram_gb is not None and total_ram_gb < requirements["ram_needed_gb"]:
                reasons.append(
                    "estimated RAM needed is about "
                    f"{format_gb(requirements['ram_needed_gb'])}, "
                    f"but this machine has {format_gb(total_ram_gb)}"
                )

            if free_disk_gb is not None and free_disk_gb < requirements["disk_needed_gb"]:
                reasons.append(
                    "estimated free disk needed is about "
                    f"{format_gb(requirements['disk_needed_gb'])}, "
                    f"but the Hugging Face cache volume has {format_gb(free_disk_gb)}"
                )

            if (
                requirements["gpu_needed_gb"] is not None
                and gpu_ram_gb is not None
                and gpu_ram_gb < requirements["gpu_needed_gb"]
            ):
                reasons.append(
                    "estimated GPU memory needed is about "
                    f"{format_gb(requirements['gpu_needed_gb'])}, "
                    f"but this GPU has {format_gb(gpu_ram_gb)}"
                )

    if reasons and not args.allow_heavy:
        stop_for_preflight(model_id, reasons, profile)

    if warnings:
        print("Preflight warning:")
        for warning in warnings:
            print(f"  - {warning}")
        print()


def print_model_recommendations():
    profile = system_profile()
    print(f"Environment: {profile['env_kind']}")
    print(
        f"System: {profile['platform']}, Python {profile['python']}, "
        f"torch {profile['torch']}, transformers {profile['transformers']}"
    )
    ram = (
        f"{profile['total_ram_gb']:.1f} GB"
        if profile["total_ram_gb"] is not None
        else "unknown"
    )
    disk = (
        f"{profile['free_disk_gb']:.1f} GB"
        if profile["free_disk_gb"] is not None
        else "unknown"
    )
    gpu_ram = (
        f", GPU memory {profile['gpu_ram_gb']:.1f} GB"
        if profile["gpu_ram_gb"] is not None
        else ""
    )
    print(f"Resources: {ram} RAM, {disk} free disk, device {profile['device']}{gpu_ram}")
    print(f"Hugging Face cache: {profile['cache_path']}")
    print()

    recommended = []
    possible = []
    unavailable = []
    for name, preset in MODEL_PRESETS.items():
        reasons, warnings = model_fit(profile, preset)
        if reasons:
            unavailable.append((name, preset, reasons))
        elif warnings:
            possible.append((name, preset, warnings))
        else:
            recommended.append((name, preset, []))

    if recommended:
        print("Recommended models:")
        for name, preset, _ in recommended:
            print(f"  python chatbot.py --model {name}")
            print(f"    {preset['label']}")

    if possible:
        print()
        print("Usable, but heavier:")
        for name, preset, warnings in possible:
            print(f"  python chatbot.py --model {name}")
            print(f"    {preset['label']} ({'; '.join(warnings)})")

    if unavailable:
        print()
        print("Not recommended in this environment:")
        for name, _, reasons in unavailable:
            print(f"  {name}: {'; '.join(reasons)}")


def preferred_device():
    # Prefer CUDA, then Apple Silicon acceleration, then plain CPU.
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def move_batch(batch, device):
    return {key: value.to(device) for key, value in batch.items()}


def load_model(model_id, args):
    config = AutoConfig.from_pretrained(model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    device = preferred_device()
    has_accelerate = importlib.util.find_spec("accelerate") is not None
    use_device_map = has_accelerate and not args.no_device_map

    # BlenderBot-style models use a seq2seq architecture; SmolLM, Qwen, and
    # TinyLlama-style chat models use a causal language model architecture.
    if config.is_encoder_decoder:
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        model.to(device)
        return tokenizer, model, config, device

    load_kwargs = {}
    if use_device_map:
        # In the modern env, accelerate can choose CPU/GPU placement and dtype.
        load_kwargs["device_map"] = "auto"
        load_kwargs["torch_dtype"] = "auto"
    else:
        # Without accelerate, keep loading simple and move the whole model to one
        # device. CPU float32 is slower but broadly compatible.
        load_kwargs["torch_dtype"] = torch.float16 if device == "cuda" else torch.float32

    model = AutoModelForCausalLM.from_pretrained(model_id, **load_kwargs)
    if not use_device_map:
        model.to(device)
    return tokenizer, model, config, model.device


def trim_messages(messages, keep_turns=6):
    # Keep the system message and the most recent turns so long chats do not grow
    # until they exceed the model context window.
    if len(messages) <= 1:
        return messages
    return messages[:1] + messages[1:][-keep_turns:]


def format_with_fallback(messages):
    lines = []
    for message in messages:
        role = message["role"]
        if role == "system":
            lines.append(f"System: {message['content']}")
        elif role == "user":
            lines.append(f"User: {message['content']}")
        else:
            lines.append(f"Chatbot: {message['content']}")
    lines.append("Chatbot:")
    return "\n".join(lines)


def build_causal_inputs(tokenizer, messages, device, max_context_tokens):
    recent_messages = trim_messages(messages)
    if getattr(tokenizer, "chat_template", None):
        # Instruct models define their preferred prompt format in the tokenizer.
        prompt = tokenizer.apply_chat_template(
            recent_messages,
            tokenize=False,
            add_generation_prompt=True,
        )
    else:
        # Plain causal models may not ship a chat template, so use a simple
        # readable transcript format instead.
        prompt = format_with_fallback(recent_messages)

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=max_context_tokens,
    )
    return move_batch(inputs, device)


def generate_causal_reply(model, tokenizer, messages, args):
    inputs = build_causal_inputs(
        tokenizer,
        messages,
        model.device,
        args.max_context_tokens,
    )
    generate_kwargs = {
        "max_new_tokens": args.max_new_tokens,
        "pad_token_id": tokenizer.eos_token_id,
    }
    if not args.no_sample:
        generate_kwargs.update(
            {
                "do_sample": True,
                "temperature": args.temperature,
                "top_p": args.top_p,
            }
        )

    outputs = model.generate(**inputs, **generate_kwargs)
    # Decode only the newly generated tokens, not the prompt we fed in.
    new_tokens = outputs[0][inputs["input_ids"].shape[-1] :]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def generate_seq2seq_reply(model, tokenizer, user_text, device, args):
    inputs = tokenizer(
        user_text,
        return_tensors="pt",
        truncation=True,
        max_length=args.max_context_tokens,
    )
    inputs = move_batch(inputs, device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=args.max_new_tokens,
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()


def chat_with_bot(tokenizer, model, config, device, args):
    messages = [{"role": "system", "content": args.system}]
    print("Type 'quit', 'exit', or 'bye' to stop.")

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in EXIT_WORDS:
            print("Chatbot: Goodbye!")
            break
        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})

        if config.is_encoder_decoder:
            response = generate_seq2seq_reply(model, tokenizer, user_text, device, args)
        else:
            response = generate_causal_reply(model, tokenizer, messages, args)

        messages.append({"role": "assistant", "content": response})
        print("Chatbot:", response)


def main():
    args = parse_args()
    if args.list_models:
        list_models()
        return
    if args.recommend_models:
        print_model_recommendations()
        return

    model_id, preset = resolve_model(args.model)
    require_transformers_version(preset)
    preflight_model(model_id, preset, args)

    print(f"Loading {model_id} ...")
    tokenizer, model, config, device = load_model(model_id, args)
    model.eval()
    print(f"Ready on {device}.")
    chat_with_bot(tokenizer, model, config, device, args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nChatbot: Goodbye!")
        sys.exit(0)
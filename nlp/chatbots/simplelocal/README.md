# Local Chatbot Starter

This folder contains a small reusable chatbot setup for running Hugging Face models locally.

It has two parts:

- `chatbot-env.sh` creates or enters a Conda environment.
- `chatbot.py` runs the chatbot and recommends models that fit the current machine.

## Files

```text
chatbot-env.sh   Create or enter the course or modern chatbot environment
chatbot.py       Reusable command-line chatbot
README.md        This guide
```

## Quick Start
First, make the environment script executable:

```bash
chmod +x chatbot-env.sh
```

From this folder, choose one environment:

```bash
./chatbot-env.sh course
```

or:

```bash
./chatbot-env.sh modern
```

The `course` environment is based on the IBM/Coursera course [Generative AI and LLMs: Architecture and Data Preparation](https://www.coursera.org/learn/generative-ai-llm-architecture-data-preparation) and is compatible with the older course-style dependency stack. The `modern` environment is for newer Hugging Face models, including Qwen3.

After the environment opens, ask the chatbot script which models make sense for the current machine:

```bash
python chatbot.py --recommend-models
```

Then run one of the recommended commands, for example:

```bash
python chatbot.py --model smollm2-360m
```

Type `quit`, `exit`, or `bye` to stop chatting.

## Hugging Face Login

You may see this warning when downloading models:

```text
Warning: You are sending unauthenticated requests to the HF Hub.
```

That warning is not fatal. Public models can still download without logging in. Logging in gives better rate limits and is required for gated/private models.

You usually do not need to install `hf` separately. This setup installs `transformers`, which installs the Hugging Face Hub package it uses for downloads.

After entering either chatbot environment, try:

```bash
hf auth login
```

If the older course environment does not have the `hf` command, use:

```bash
huggingface-cli login
```

Create a read token here:

```text
https://huggingface.co/settings/tokens
```

You can also set a token for just the current terminal session:

```bash
export HF_TOKEN="hf_your_token_here"
python chatbot.py --model smollm2-360m
```

`chatbot.py` does not have a `--hf-token` option. That is intentional: `transformers` and `huggingface_hub` automatically use either your saved login token or the `HF_TOKEN` environment variable. Avoid putting tokens directly into commands when possible, since they can end up in shell history.


## Environment Choices

### Course Environment

The `course` environment is based on the IBM/Coursera course [Generative AI and LLMs: Architecture and Data Preparation](https://www.coursera.org/learn/generative-ai-llm-architecture-data-preparation) and is compatible with the older course-style dependency stack.  Use this when you want compatibility with the older course-style dependency stack. (This reusable chatbot setup is not part of the Coursera course, though the simple chatbot function in the lab notebook from module 1 was used as a jumping-off point for it.)

```bash
./chatbot-env.sh course
```

This environment pins the important older packages, including:

- `transformers==4.42.1`
- `numpy==1.26.4`
- `torch==2.2.2`
- `torchtext==0.17.2`

Good starter models in this environment:

```bash
python chatbot.py --model smollm2-135m
python chatbot.py --model smollm2-360m
python chatbot.py --model qwen2-0.5b
python chatbot.py --model qwen2.5-0.5b
python chatbot.py --model blenderbot-400m
```

### Modern Environment

Use this for newer Hugging Face models, including Qwen3.

```bash
./chatbot-env.sh modern
```

This environment installs newer packages, including:

- `transformers>=4.51.0`
- `tokenizers>=0.21.0`
- `accelerate`
- `safetensors`
- `sentencepiece`
- current PyTorch

Good starter models in this environment:

```bash
python chatbot.py --model smollm2-360m
python chatbot.py --model qwen2.5-0.5b
python chatbot.py --model tinyllama-1.1b
python chatbot.py --model qwen3-4b
```

## Model Recommendations

Run:

```bash
python chatbot.py --recommend-models
```

The script checks:

- course vs modern environment
- installed `transformers` version
- operating system and processor type
- available RAM
- available disk space
- CUDA/GPU availability when present

It then prints commands for models that should be reasonable on that system.

## Safety Preflight

When you run a model, `chatbot.py` checks whether the model looks safe for the current machine before downloading or loading model weights.

For built-in presets, it uses the local model requirements in `chatbot.py`.

For a direct Hugging Face model id, it asks Hugging Face for file-size metadata first. This is a lightweight metadata check, not a full model download.

If the model looks too large, the script stops and suggests smaller alternatives:

```bash
python chatbot.py --model qwen3-4b
```

You can override the safety check when you know what you are doing:

```bash
python chatbot.py --model qwen3-4b --allow-heavy
```

## Listing All Presets

To see every built-in model preset:

```bash
python chatbot.py --list-models
```

You can also pass a Hugging Face model id directly:

```bash
python chatbot.py --model HuggingFaceTB/SmolLM2-360M-Instruct
```

## Useful Options

Limit response length:

```bash
python chatbot.py --model smollm2-360m --max-new-tokens 80
```

Allow more conversation history:

```bash
python chatbot.py --model qwen3-4b --max-context-tokens 4096
```

Use deterministic generation:

```bash
python chatbot.py --model qwen2-0.5b --no-sample
```

Change the system prompt:

```bash
python chatbot.py --model smollm2-360m --system "You are a friendly Python tutor."
```

## Resetting An Environment

To delete and rebuild one of the local Conda environments:

```bash
./chatbot-env.sh course --reset
```

or:

```bash
./chatbot-env.sh modern --reset
```

Each environment is created inside the current folder:

```text
.conda-chatbot-course
.conda-chatbot-modern
```

These folders can be large because they contain Python packages and downloaded dependencies.

## Limitations

This setup is intentionally simple. It is a local command-line chatbot, not a full assistant system.

The model does not have true memory. `chatbot.py` keeps a short list of recent messages and sends that transcript back to the model on each turn. If the conversation gets long, older turns are dropped so the prompt does not exceed the model context window.

Small models may also ignore parts of the transcript or fall back to generic chatbot answers. For example, a small model may say it cannot remember earlier messages even when the recent transcript is still present. This usually improves with stronger models and clearer prompting, but it is still a limitation of small local chat models.

This setup also does not have tools. It cannot inspect your files, run commands, search the web, call APIs, or verify its own answers unless that capability is added separately.

To go beyond this limited chatbot, common next steps include:

- use a stronger instruction-tuned model
- keep a running summary of older conversation
- save useful facts or preferences to a local file or database
- retrieve relevant notes/files before each response
- add tool use for search, code execution, file inspection, or APIs
- add a control loop that plans, gathers context, checks results, and then answers

In short: this project gives you a small local chat loop. A more capable assistant needs a stronger model plus memory, retrieval, tools, and orchestration around the model.


## Notes

- The first run of a model may take time because Hugging Face needs to download model files.
- Smaller models are faster and easier to run, but less capable.
- Larger models usually need more RAM, more disk space, and ideally a GPU.
- `qwen3-4b` requires the modern environment because Qwen3 needs newer `transformers`.
- The chatbot keeps conversation history bounded so long sessions do not grow forever.
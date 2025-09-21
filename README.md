# LLama Local Guide

This repository documents a reproducible workflow to run modern open weights locally on a machine with (my exact setup):

- CPU: 32 GB RAM
- GPU: 6 GB VRAM (consumer card, limited for large models)
- OS: Windows 11 Home Single Language Version 24H2 OS build 26100.6584
- Goal: run 7B-13B models with quantization and optional GPU offload, and publish the steps so others can reproduce them.

---

## Table of contents

- Prerequisites
- Quick install examples
- Models tested
- Benchmarks
- Example commands
- Notes and tips
- Repository layout
- Contributing

---

## Prerequisites

- Python 3.10+
- Git
- Build tools: CMake, make, gcc/clang (for building native code like `llama.cpp`)
- CUDA toolkit and matching NVIDIA drivers if you plan to use GPU acceleration
- Sufficient free disk space to store model files (several GB per model)

---

## Quick install examples

### 1. Build `llama.cpp` (CPU-first, GGUF)

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make -j$(nproc)
```

### 2. Clone text-generation-webui (optional web UI)

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
# follow the repo README for Python venv and CUDA setup
```

---

## Models tested (so far)

| Model | Params | Typical format | Approx RAM (q4) | VRAM | Notes |
|---|---:|---|---:|---:|---|
| LLaMA-2 8B | 8B | GPTQ / GGUF q4 | ~10-12 GB | ~4-6 GB | Might need CPU split on 6 GB cards |
| LLaMA-2 13B | 13B | GGUF q4 | ~15-18 GB | CPU-only practical | Best on CPU with 32 GB, slower inference |

*Numbers are approximate and vary with quantization, context size, and loader.*

---

## Benchmarks (rough tokens per second)

| Model | Quant | CPU (32 GB) | GPU offload (6 GB) |
|---|---:|---:|---:|
| LLaMA-2 8B | GPTQ 4bit | ~4 tok/s | ~10-20 tok/s |
| LLaMA-2 13B | q4 | ~2-5 tok/s | not practical on 6 GB |

*Benchmarks depend on CPU threads, OS, CUDA, and context length.*

---

## Example commands

### Run a GGUF quantized model with the `llama.cpp` binary

```bash
# run binary built from llama.cpp
./main -m models/mistral-7b-q4_k_m.gguf -p "Summarize the state of local LLMs." -n 128 --threads 8 --ctx_size 2048
```

### Start text-generation-webui

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
# set up venv and dependencies per repo README
python server.py --model /path/to/model
```

### Example: use ExLlama/ExLlamaV2 via a loader in the web UI

```bash
# invocation depends on the UI wrapper. This is an example placeholder
python example_inference.py --model models/llama-2-8b-gptq --prompt "Write a short poem."
```

---

## Notes and tips

- For 6 GB VRAM, prefer 7B models or aggressively quantized 8B variants.
- 13B runs best on CPU with 32 GB RAM using 4-bit quantization. Expect lower throughput compared to GPU.
- Converting and quantizing model weights can use more RAM than final inference. Convert on a machine with spare memory if needed.
- Long context windows increase memory due to KV cache; reduce context if you hit out-of-memory.
- Use Q4_K_M, Q4_0, or GPTQ 4-bit formats for a balance of quality and size. AWQ and AutoGPTQ are other quantizers to try.
- Always check the model license on the host (Hugging Face, model page) before downloading.

---

## Repository layout (suggested)

```
.
├── README.md
├── scripts/
│   ├── install.sh
│   ├── convert_hf_to_gguf.sh
│   ├── run_mistral.sh
│   └── benchmark.py
├── configs/
│   ├── exllama_config.json
│   └── llama_cpp_config.json
└── results/
    ├── benchmarks.md
    └── memory-logs/
```

---

## Contributing

- Fork and open PRs with improved scripts, configs, and reproducible benchmarks.
- Add notes on specific OS, drivers, and CUDA versions when reporting OOM or performance issues.
- Prefer small, tested PRs that add value: example config, small script, or benchmark result.

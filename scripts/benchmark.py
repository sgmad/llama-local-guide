#!/usr/bin/env python3
import subprocess, time, statistics

# Choose which model to benchmark
model = "models/llama-3.1-8b-q4.gguf"

cmd = [
    "./llama.cpp/main",
    "-m", model,
    "-p", "Benchmarking...",
    "-n", "128",
    "--threads", "8"
]

runs = []
for i in range(3):
    start = time.time()
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    elapsed = time.time() - start
    runs.append(128 / elapsed)

print("Tokens/sec:", statistics.mean(runs))

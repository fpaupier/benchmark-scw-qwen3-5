import os
import sys
import time
import statistics
from datetime import datetime, timezone

from openai import OpenAI

BASE_URL = os.environ.get("SCW_BASE_URL", "").rstrip("/") + "/v1"
NUM_RUNS = 15
PROMPT = "What is the capital of France?"
SYSTEM_PROMPT = "You are a helpful assistant"
OUTPUT_FILE = "results/benchmark_results.md"

MODELS = [
    {
        "name": "qwen3.5-397b-a17b",
        "temperature": 0.6,
        "top_p": 0.95,
        "max_tokens": 2048,
        "presence_penalty": 0,
        "reasoning_effort": "low",
        "response_format": {"type": "text"},
    },
    {
        "name": "qwen3-235b-a22b-instruct-2507",
        "temperature": 0.7,
        "top_p": 0.8,
        "max_tokens": 2048,
        "presence_penalty": 0,
        "response_format": {"type": "text"},
    },
]


def run_single_inference(client, model_config):
    kwargs = {
        "model": model_config["name"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT},
        ],
        "max_tokens": model_config["max_tokens"],
        "temperature": model_config["temperature"],
        "top_p": model_config["top_p"],
        "presence_penalty": model_config["presence_penalty"],
        "stream": False,
        "response_format": model_config["response_format"],
    }
    if "reasoning_effort" in model_config:
        kwargs["reasoning_effort"] = model_config["reasoning_effort"]

    start = time.perf_counter()
    response = client.chat.completions.create(**kwargs)
    elapsed = time.perf_counter() - start

    text = response.choices[0].message.content
    return elapsed, text


def run_benchmark(client, model_config):
    name = model_config["name"]
    results = []
    for i in range(NUM_RUNS):
        try:
            elapsed, text = run_single_inference(client, model_config)
            print(f"  [{name}] Run {i + 1}/{NUM_RUNS}: {elapsed:.3f}s")
            results.append({"run": i + 1, "time": elapsed, "response": text})
        except Exception as e:
            print(f"  [{name}] Run {i + 1}/{NUM_RUNS}: ERROR - {e}")
            results.append({"run": i + 1, "time": None, "response": str(e)})
    return results


def generate_markdown(all_results):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    model_names = list(all_results.keys())

    # Compute stats per model
    stats = {}
    for name in model_names:
        times = [r["time"] for r in all_results[name] if r["time"] is not None]
        if times:
            stats[name] = {
                "mean": statistics.mean(times),
                "median": statistics.median(times),
                "min": min(times),
                "max": max(times),
                "stdev": statistics.stdev(times) if len(times) > 1 else 0.0,
            }
        else:
            stats[name] = {k: None for k in ("mean", "median", "min", "max", "stdev")}

    lines = []
    lines.append("# Benchmark Results: Qwen Model Inference Speed\n")
    lines.append(f"**Date:** {now}  ")
    lines.append(f'**Prompt:** "{PROMPT}"  ')
    lines.append(f"**Runs per model:** {NUM_RUNS}\n")

    # --- Summary ---
    lines.append("## Summary\n")
    lines.append(f"| Metric | {' | '.join(model_names)} |")
    lines.append(f"|---|{'---|' * len(model_names)}")
    for metric, label in [
        ("mean", "Mean latency"),
        ("median", "Median latency"),
        ("min", "Min latency"),
        ("max", "Max latency"),
        ("stdev", "Std deviation"),
    ]:
        vals = []
        for name in model_names:
            v = stats[name][metric]
            vals.append(f"{v:.3f}s" if v is not None else "N/A")
        lines.append(f"| {label} | {' | '.join(vals)} |")

    # Observed difference
    means = [stats[n]["mean"] for n in model_names]
    if all(m is not None for m in means) and means[1] != 0:
        diff_pct = ((means[0] - means[1]) / means[1]) * 100
        if diff_pct > 0:
            lines.append(
                f"\n**Observed difference:** {model_names[0]} is {abs(diff_pct):.1f}% "
                f"slower than {model_names[1]} on average."
            )
        else:
            lines.append(
                f"\n**Observed difference:** {model_names[0]} is {abs(diff_pct):.1f}% "
                f"faster than {model_names[1]} on average."
            )

    # --- Comparison table ---
    lines.append("\n## Comparison Table\n")
    lines.append(f"| Run | {' | '.join(model_names)} |")
    lines.append(f"|---|{'---|' * len(model_names)}")
    for i in range(NUM_RUNS):
        vals = []
        for name in model_names:
            t = all_results[name][i]["time"]
            vals.append(f"{t:.3f}s" if t is not None else "ERROR")
        lines.append(f"| {i + 1} | {' | '.join(vals)} |")

    # --- Per-model details ---
    lines.append("\n## Per-Model Details\n")
    for name in model_names:
        lines.append(f"### {name}\n")
        lines.append("| Run | Time (s) | Response (truncated) |")
        lines.append("|---|---|---|")
        for r in all_results[name]:
            t = f"{r['time']:.3f}" if r["time"] is not None else "ERROR"
            resp = r["response"][:80].replace("\n", " ").replace("|", "\\|")
            lines.append(f"| {r['run']} | {t} | {resp} |")
        lines.append("")

    return "\n".join(lines)


def main():
    api_key = os.environ.get("SCW_SECRET_KEY")
    base_url = os.environ.get("SCW_BASE_URL")
    if not api_key:
        print("ERROR: SCW_SECRET_KEY environment variable is not set.")
        sys.exit(1)
    if not base_url:
        print("ERROR: SCW_BASE_URL environment variable is not set.")
        sys.exit(1)

    client = OpenAI(base_url=BASE_URL, api_key=api_key)
    all_results = {}

    for model_config in MODELS:
        name = model_config["name"]
        print(f"\nBenchmarking {name}...")
        all_results[name] = run_benchmark(client, model_config)

    md = generate_markdown(all_results)
    os.makedirs("results", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(md)

    print(f"\nResults written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

# Benchmark: Qwen3.5 vs Qwen3 on Scaleway

Inference speed benchmark comparing `qwen3.5-397b-a17b` and `qwen3-235b-a22b-instruct-2507` on [Scaleway Generative API](https://console.scaleway.com/generative-api/models/).

15 iterations per model, wall-clock latency, simple prompt, no reasoning.

## Setup

1. Copy the environment file and fill in your credentials:

```sh
cp .env.example .env
```

2. Edit `.env` with your values from the [Scaleway console](https://console.scaleway.com/generative-api/models/):

```
SCW_SECRET_KEY=your-iam-api-key
SCW_BASE_URL=https://api.scaleway.ai/your-project-id
```

## Run

```sh
docker compose up --build
```

Results are written to `results/benchmark_results.md`.

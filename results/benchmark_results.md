# Benchmark Results: Qwen Model Inference Speed

**Date:** 2026-03-30 14:03:20 UTC  
**Prompt:** "What is the capital of France?"  
**Runs per model:** 5

## Summary

| Metric | qwen3.5-397b-a17b | qwen3-235b-a22b-instruct-2507 |
|---|---|---|
| Mean latency | 3.095s | 0.170s |
| Median latency | 2.925s | 0.150s |
| Min latency | 2.367s | 0.118s |
| Max latency | 4.442s | 0.259s |
| Std deviation | 0.804s | 0.060s |

**Observed difference:** qwen3.5-397b-a17b is 1723.0% slower than qwen3-235b-a22b-instruct-2507 on average.

## Comparison Table

| Run | qwen3.5-397b-a17b | qwen3-235b-a22b-instruct-2507 |
|---|---|---|
| 1 | 2.367s | 0.200s |
| 2 | 2.632s | 0.118s |
| 3 | 4.442s | 0.259s |
| 4 | 3.111s | 0.150s |
| 5 | 2.925s | 0.122s |

## Per-Model Details

### qwen3.5-397b-a17b

| Run | Time (s) | Response (truncated) |
|---|---|---|
| 1 | 2.367 |   The capital of France is **Paris**. |
| 2 | 2.632 |   The capital of France is **Paris**. |
| 3 | 4.442 |   The capital of France is **Paris**. |
| 4 | 3.111 |   The capital of France is **Paris**. |
| 5 | 2.925 |   The capital of France is **Paris**. |

### qwen3-235b-a22b-instruct-2507

| Run | Time (s) | Response (truncated) |
|---|---|---|
| 1 | 0.200 | The capital of France is Paris. |
| 2 | 0.118 | The capital of France is Paris. |
| 3 | 0.259 | The capital of France is Paris. |
| 4 | 0.150 | The capital of France is Paris. |
| 5 | 0.122 | The capital of France is Paris. |

# Benchmark Results: Qwen Model Inference Speed

**Date:** 2026-03-30 14:07:52 UTC  
**Prompt:** "What is the capital of France?"  
**Runs per model:** 15

## Summary

| Metric | qwen3.5-397b-a17b | qwen3-235b-a22b-instruct-2507 |
|---|---|---|
| Mean latency | 2.336s | 0.315s |
| Median latency | 1.580s | 0.303s |
| Min latency | 1.287s | 0.149s |
| Max latency | 7.869s | 0.615s |
| Std deviation | 1.761s | 0.148s |

**Observed difference:** qwen3.5-397b-a17b is 642.4% slower than qwen3-235b-a22b-instruct-2507 on average.

## Comparison Table

| Run | qwen3.5-397b-a17b | qwen3-235b-a22b-instruct-2507 |
|---|---|---|
| 1 | 1.949s | 0.303s |
| 2 | 1.467s | 0.221s |
| 3 | 4.651s | 0.319s |
| 4 | 2.086s | 0.441s |
| 5 | 1.607s | 0.184s |
| 6 | 7.869s | 0.328s |
| 7 | 1.580s | 0.177s |
| 8 | 1.478s | 0.180s |
| 9 | 1.561s | 0.474s |
| 10 | 3.147s | 0.511s |
| 11 | 1.571s | 0.239s |
| 12 | 1.579s | 0.615s |
| 13 | 1.684s | 0.427s |
| 14 | 1.517s | 0.149s |
| 15 | 1.287s | 0.151s |

## Per-Model Details

### qwen3.5-397b-a17b

| Run | Time (s) | Response (truncated) |
|---|---|---|
| 1 | 1.949 |   The capital of France is **Paris**. |
| 2 | 1.467 |   The capital of France is **Paris**. |
| 3 | 4.651 |   The capital of France is **Paris**. |
| 4 | 2.086 |   The capital of France is **Paris**. |
| 5 | 1.607 |   The capital of France is **Paris**. |
| 6 | 7.869 |   The capital of France is **Paris**. |
| 7 | 1.580 |   The capital of France is **Paris**. |
| 8 | 1.478 |   The capital of France is **Paris**. |
| 9 | 1.561 |   The capital of France is **Paris**. |
| 10 | 3.147 |   The capital of France is **Paris**. |
| 11 | 1.571 |   The capital of France is **Paris**. |
| 12 | 1.579 |   The capital of France is **Paris**. |
| 13 | 1.684 |   The capital of France is **Paris**. |
| 14 | 1.517 |   The capital of France is **Paris**. |
| 15 | 1.287 |   The capital of France is **Paris**. |

### qwen3-235b-a22b-instruct-2507

| Run | Time (s) | Response (truncated) |
|---|---|---|
| 1 | 0.303 | The capital of France is Paris. |
| 2 | 0.221 | The capital of France is Paris. |
| 3 | 0.319 | The capital of France is Paris. |
| 4 | 0.441 | The capital of France is Paris. |
| 5 | 0.184 | The capital of France is Paris. |
| 6 | 0.328 | The capital of France is Paris. |
| 7 | 0.177 | The capital of France is Paris. |
| 8 | 0.180 | The capital of France is Paris. |
| 9 | 0.474 | The capital of France is Paris. |
| 10 | 0.511 | The capital of France is Paris. |
| 11 | 0.239 | The capital of France is Paris. |
| 12 | 0.615 | The capital of France is Paris. |
| 13 | 0.427 | The capital of France is Paris. |
| 14 | 0.149 | The capital of France is Paris. |
| 15 | 0.151 | The capital of France is Paris. |

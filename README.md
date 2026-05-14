# Environmental Index - Multi-Agent LLM Benchmark Task

A SwarmBench benchmark task designed to evaluate the reasoning, coordination, extraction, and synthesis capabilities of Large Language Models (LLMs) in multi-agent environments.

---

## Overview

This benchmark simulates a complex environmental risk assessment workflow where multiple agents analyze domain-specific environmental reports and collaboratively synthesize structured outputs.

The task is intentionally designed to demonstrate the performance gap between:
- Single-agent execution
- Multi-agent collaborative execution

---

## Objective

Agents must:

1. Analyze multiple environmental PDF reports
2. Extract environmental stress indicators
3. Compute structured environmental risk metrics
4. Generate a final synthesized JSON output

---

## Domains Covered

- Water pollution
- Air pollution
- Soil degradation
- Forest conservation
- Ecosystem stress
- Environmental contamination

---

## Output Metrics

The benchmark evaluates:
- environmental_stress_score
- high_stress_count
- average_stress_score
- urgent_priority_count
- most_common_threat

---

## Multi-Agent Design

The task follows a fan-out → synthesize architecture.

### Specialist Agents
Each specialist independently analyzes a subset of reports.

### Reducer Agent
The reducer synthesizes intermediate outputs into final benchmark metrics.

This architecture evaluates:
- Distributed reasoning
- Cross-document synthesis
- Information reconciliation
- Context management
- Coordination efficiency

---

## Benchmark Goal

The benchmark is designed so that:

### Single-Agent Systems Struggle With:
- Context overload
- Missed evidence
- Inconsistent synthesis
- Reduced evidence coverage

### Multi-Agent Systems Perform Better Through:
- Parallel extraction
- Domain specialization
- Coordinated synthesis
- Better context distribution

---

## Repository Structure

```text
.
├── instruction.md
├── decomposition.yaml
├── task.toml
├── README.md
│
├── environment/
│   └── input_artifacts/
│
├── tests/
│   ├── verify.py
│   └── test.sh
│
├── solution/
│   ├── solve.sh
│   └── derivation.md
│
└── execution_logs/

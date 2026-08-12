# BhoomiAI v0.2.0 — Integrated Benchmark and Quality Release

## Overview

BhoomiAI v0.2.0 expands the initial open-source foundation into a measurable agriculture-security evaluation workflow. The release adds a working CLI, structured integrated benchmark evaluation, machine-readable and Markdown reports, configurable quality thresholds, and baseline regression tracking.

## Highlights

- working `bhoomiai` CLI
- integrated evaluation for agriculture content security, recommendation safety, access control, privacy redaction, and explicit workflow-policy cases
- structured evaluator traces and reproducible benchmark metrics
- JSON and Markdown benchmark reports
- expected-vs-actual decision matrix
- failed-case diagnostics
- configurable overall and category-level quality thresholds
- reviewed v0.2.0 benchmark baseline
- regression tracking for newly failing or missing baseline cases
- Benchmark Quality GitHub Actions workflow with report artifact upload

## Command-Line Examples

```bash
bhoomiai validate-content examples/sample.txt
bhoomiai check-access farmer view_own_farm
bhoomiai run-integrated-benchmark benchmarks/agriculture_security_cases.jsonl
bhoomiai generate-benchmark-report benchmarks/agriculture_security_cases.jsonl --output-dir artifacts/benchmark
```

## Data Safety

All public examples and benchmark cases use synthetic, independently created, properly licensed, or otherwise public-safe material. The repository must not contain identifiable farmer information, private farm coordinates, credentials, confidential FPO records, production secrets, restricted market information, or proprietary third-party material without permission.

## Responsible Use

BhoomiAI reference modules are intended for development, testing, and evaluation. They do not replace agronomists, extension officers, product-label directions, local regulations, verified field observations, weather authorities, market authorities, or professional judgement. This release is not a claim of production security certification or independent audit.

## Compatibility

Python 3.10 or newer.

## Maintained By

Optficial Labs Pvt Ltd., Hyderabad, India

Website: https://optficial.ai/

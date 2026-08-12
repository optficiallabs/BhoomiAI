# BhoomiAI Benchmark Methodology

## Purpose

The BhoomiAI agriculture security benchmark is a public, reproducible evaluation set for defensive agriculture workflows. It is intended to measure whether reference components produce the expected allow, deny, block, review, or redact decisions across representative security and governance scenarios.

## Data policy

Benchmark cases must use synthetic, independently created, properly licensed, or otherwise public-safe material. Cases must not include identifiable farmer information, private farm coordinates, credentials, confidential FPO records, production secrets, restricted third-party data, or proprietary material without permission.

## Case structure

Each JSONL case includes a stable case identifier, category, scenario, evaluator type, structured input, and expected decision. Stable identifiers support baseline comparison and regression tracking across repository changes.

## Current coverage

The benchmark covers normal guidance, content security, recommendation safety, privacy, market integrity, access control, human review, weather integrity, field verification, and multi-step workflow risk.

## Evaluation

Cases are routed through the integrated evaluator to the relevant defensive module. Unsupported evaluator types fail closed to human review. Results record the expected decision, actual decision, correctness, evaluator trace, and category.

## Metrics

The reporting layer calculates overall accuracy and per-category accuracy. Reports also include expected-versus-actual decision matrices and failed-case diagnostics.

## Quality gates

Pull requests are evaluated against configured overall and category-level thresholds. Required categories must be present. Baseline regression checks detect previously passing cases that begin failing, missing baseline cases, and changed decisions.

## Review requirements

New benchmark cases should describe a realistic defensive workflow, have an unambiguous expected decision, add coverage beyond existing cases, and remain public-safe. Changes should pass Tests, Dependency Review, Release Readiness, and Benchmark Quality before merge.

## Interpretation

Benchmark results measure behaviour on the documented public test set. They are not a claim of production security certification, agronomic correctness for every location, independent audit, or suitability for autonomous high-risk decision making.

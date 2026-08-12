# Changelog

All notable changes to BhoomiAI will be documented here.

## [Unreleased]

### Added
- `CITATION.cff` with project citation metadata
- expanded agriculture security benchmark from 10 to 25 synthetic/public-safe cases
- benchmark readiness test covering 25 unique cases and 10 workflow categories

### Changed
- README now documents benchmark coverage and citation guidance

## [0.2.0] - 2026-08-12

### Added
- working `bhoomiai` command-line interface
- integrated agriculture benchmark evaluation across content security, recommendation safety, access control, privacy redaction, and workflow-policy cases
- expanded structured benchmark dataset with evaluator inputs
- benchmark execution and overall/per-category metrics
- JSON and Markdown benchmark report generation
- configurable overall and category-level quality thresholds
- reviewed benchmark baseline and regression comparison
- Benchmark Quality GitHub Actions workflow with report artifacts
- v0.2.0 maturity tests

### Changed
- expanded the README with CLI and benchmark-quality workflows
- package version updated to 0.2.0 and CLI entry point registered

### Security
- unsupported evaluator types fail closed to review
- public examples and benchmark cases remain synthetic or otherwise public-safe

## [0.1.0] - 2026-08-12

### Added
- open-source project documentation and Apache 2.0 licensing
- defensive learning-content-style checks adapted for agriculture workflows
- recommendation-safety reference rules
- role-based access-control reference module
- privacy-aware farm logging and recursive redaction
- synthetic agriculture security benchmark cases
- benchmark validation helpers
- unit tests for core defensive modules
- automated Tests workflow
- Release Readiness workflow
- Codex maintainer workflow guidance

### Security
- public examples and benchmark cases are synthetic or otherwise public-safe
- reference controls are intended for evaluation and development, not production certification

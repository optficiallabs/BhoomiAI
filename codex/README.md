# Codex Maintainer Workflow

This directory documents how maintainers may use Codex to assist with BhoomiAI development while preserving human review and public-data safety.

## Suitable Tasks

- understand repository structure and locate relevant modules
- convert approved issues into implementation plans
- draft or refactor code on feature branches
- add and improve unit tests
- review diffs for correctness and maintainability
- update documentation and release notes
- run release-readiness checks and summarise failures

## Required Boundaries

Codex-assisted changes must remain subject to maintainer review. Do not place identifiable farmer information, private farm coordinates, credentials, confidential FPO records, proprietary datasets, restricted market information, or production secrets in prompts, test fixtures, examples, commits, or public benchmark files.

Agricultural recommendations can affect real-world decisions. Reference modules and synthetic benchmarks in this repository are not a substitute for agronomists, local regulations, label directions, safety requirements, or verified field observations.

## Maintainer Checklist

1. Work from a clearly scoped issue or release task.
2. Confirm all data used is synthetic, independently created, properly licensed, or otherwise public-safe.
3. Make changes on a branch and keep commits focused.
4. Run unit tests and release-readiness checks.
5. Review security, privacy, recommendation-safety, and documentation implications.
6. Require human approval before merge or release.

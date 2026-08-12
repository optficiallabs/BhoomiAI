# BhoomiAI

BhoomiAI is an open-source agriculture technology project for localized farm intelligence, crop-risk assessment, soil-aware guidance, weather and market context, multilingual farmer support, and secure agriculture workflows for farmers, FPOs, extension teams, and research communities.

## Purpose

BhoomiAI is designed to help agricultural users understand changing farm conditions and make better-informed decisions while keeping safety, traceability, data minimisation, and human oversight central to the workflow.

## Core Areas

- localized crop and farm guidance
- crop-condition and disease-risk assessment
- soil-aware planning
- weather-context interpretation
- market-information workflows
- multilingual and voice-first farmer interaction
- photo-assisted crop issue reporting
- farm and field record management
- FPO and extension-team coordination
- secure access to agriculture data and recommendations

## Security and Responsible Use

The public repository must not contain identifiable farmer information, confidential farm records, private credentials, production secrets, restricted third-party data, or proprietary material without permission.

Public examples and benchmark cases should use synthetic, independently created, properly licensed, or otherwise public-safe data.

BhoomiAI provides reference utilities and open-source evaluation workflows. It does not replace agronomists, local extension services, pesticide labels, regulatory requirements, weather authorities, market authorities, or professional judgement.

## Open-Source Structure

The project includes reusable components for agriculture-content validation, recommendation-safety checks, role-based access control, privacy-aware logging, integrated benchmark evaluation, benchmark reporting, threshold gates, regression tracking, tests, and developer workflows.

## Getting Started

```bash
git clone https://github.com/optficiallabs/BhoomiAI.git
cd BhoomiAI
python -m pip install -e .
python -m unittest discover -s tests -p "test_*.py"
```

## CLI

After installation, the `bhoomiai` command provides open-source reference utilities.

Validate agriculture content:

```bash
bhoomiai validate-content examples/sample.txt
```

Check a role/action permission:

```bash
bhoomiai check-access farmer view_own_farm
```

Run structured benchmark cases through the integrated evaluator:

```bash
bhoomiai run-integrated-benchmark benchmarks/agriculture_security_cases.jsonl
```

Include per-case traces:

```bash
bhoomiai run-integrated-benchmark benchmarks/agriculture_security_cases.jsonl --include-results
```

Generate JSON and Markdown benchmark reports:

```bash
bhoomiai generate-benchmark-report benchmarks/agriculture_security_cases.jsonl --output-dir artifacts/benchmark
```

The `Benchmark Quality` GitHub Actions workflow enforces configured overall and category-level thresholds, compares results against the reviewed baseline, and uploads report artifacts for pull-request review.

## Benchmark Coverage

The public agriculture security benchmark currently contains 25 synthetic, public-safe cases covering normal guidance, content security, recommendation safety, privacy, market integrity, access control, human review, weather integrity, field verification, and multi-step workflow risk. Benchmark changes are evaluated through the integrated evaluator and existing quality/regression gates before merge.

## Project Team

- **Dr. Asadi Srinivasulu — Chief Advisor:** research and technical direction, architecture, evaluation design, validation, and strategic guidance.
- **Dr. Tarkeswar Barua — R&D Head:** research planning, technical supervision, security testing, benchmark validation, and quality assurance.
- **Dr. Pradeep G — Project Coordinator:** project execution, benchmark/scenario coordination, testing, documentation, reporting, release activities, and milestones.
- **Goddindla Nagarjuna — Development and Testing Support:** implementation, test development, debugging, and component validation.
- **Harini Priyanshu Adike — Testing, Documentation and Validation Support:** functional testing, benchmark verification, documentation, and result validation.
- **Paila Sharmila — Research and Domain Workflow Support:** agriculture workflow analysis, use-case preparation, research support, and domain validation.
- **Mullaa Sufiyan Khan — Integration, Security Testing and Reproducibility Support:** integration, defensive security testing, reproducibility checks, and benchmark execution.

See `TEAM.md` for full roles and responsibilities.

## Citation

If you use BhoomiAI, its benchmark, or its evaluation utilities in research or technical work, please cite the project using the metadata in `CITATION.cff`.

## Contributing

Please review `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` before contributing.

## Licence

BhoomiAI is released under the Apache License 2.0.

## Maintained By

Optficial Labs Pvt Ltd., Hyderabad, India

Website: https://optficial.ai/

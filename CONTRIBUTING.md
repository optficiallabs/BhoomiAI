# Contributing to BhoomiAI

Thank you for contributing to BhoomiAI.

## Development Principles

- keep changes focused and reviewable
- use synthetic, independently created, properly licensed, or otherwise public-safe data
- never commit credentials, secrets, identifiable farmer information, confidential farm records, restricted market data, or proprietary third-party content without permission
- add or update tests for functional changes
- document behaviour that affects safety, access control, recommendations, benchmarks, or public interfaces

## Workflow

1. Open or select an issue.
2. Create a focused branch.
3. Implement the change with tests and documentation where appropriate.
4. Run the test suite locally.
5. Open a pull request describing the change, validation performed, and any safety implications.

## Testing

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Responsible Agriculture Guidance

Contributions involving crop protection, chemical use, weather risk, market information, or agronomic recommendations must be framed as reference or decision-support workflows. They must not bypass labels, local regulations, authorised extension guidance, or professional judgement.

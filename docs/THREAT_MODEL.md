# BhoomiAI Threat Model

## Scope

This document describes the main defensive risks considered by the public BhoomiAI reference repository. It covers open-source agriculture workflow components, benchmark data, contributor changes, and evaluation tooling. It does not represent a production deployment assessment.

## Assets to protect

- farmer and farm information
- private field locations and identifiers
- FPO and institutional records
- credentials, API keys, tokens, and secrets
- integrity of agriculture guidance and advisories
- benchmark integrity and expected decisions
- repository and CI workflow integrity

## Primary threat areas

### Sensitive-data exposure
Public logs, examples, bug reports, or benchmark cases could accidentally contain identifiable farmer information, private coordinates, credentials, or confidential records. BhoomiAI uses privacy-aware redaction helpers and requires public-safe test material.

### Unsafe or insufficiently verified recommendations
High-risk pesticide, herbicide, fungicide, or chemical-dose guidance may be unsafe without appropriate label references or local context. Such cases should route to review rather than being treated as unrestricted guidance.

### Access-control violations
Users may attempt actions outside their assigned role, including management, publication, or bulk-data operations. Reference access-control checks use explicit allow lists and deny unknown permissions.

### Instruction or content manipulation
Untrusted content may attempt to bypass safety rules, request restricted records, or manipulate workflow decisions. Content-security checks are designed to identify representative unsafe patterns and fail safely.

### Market and weather misinformation
Unverified price guarantees, fabricated weather alerts, or misleading external claims can influence farm decisions. Workflows should preserve source verification and human review for high-impact uncertainty.

### Benchmark tampering or regression
Changes may weaken expected defensive behaviour while still appearing technically valid. Stable benchmark identifiers, thresholds, baseline comparison, CI checks, and pull-request review are used to detect regressions.

### Supply-chain and contributor risk
Dependencies, code changes, or workflow modifications may introduce vulnerabilities or bypass controls. Dependency Review, protected branches, mandatory pull requests, required status checks, and CODEOWNERS support repository governance.

## Trust boundaries

Inputs from users, uploaded content, external data sources, market information, weather information, and contributor-supplied benchmark cases should be treated as untrusted until validated. CI results support review but do not replace maintainer judgement.

## Security posture

BhoomiAI follows a defensive, fail-closed approach where uncertainty or unsupported evaluator paths should route to review. The public repository avoids real sensitive data and is designed for reproducible development and evaluation, not autonomous production control.

## Out of scope

The public threat model does not claim coverage of every production infrastructure risk, cloud configuration, endpoint security control, field-device security issue, regulatory requirement, or agronomic hazard. Production deployments require separate environment-specific security and domain review.

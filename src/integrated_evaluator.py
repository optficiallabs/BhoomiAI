"""Integrated evaluator for BhoomiAI agriculture security benchmarks."""

from __future__ import annotations

from .access_control import authorise
from .content_security import scan_agriculture_content
from .recommendation_safety import evaluate_recommendation
from .secure_logging import redact_record


def evaluate_case(case: dict) -> dict:
    evaluator = str(case.get("evaluator") or "").strip()
    payload = case.get("input") or {}

    if evaluator == "content_security":
        result = scan_agriculture_content(str(payload.get("text") or ""))
        return {
            "decision": "allow" if result["safe"] else "block",
            "reason": "content_safe" if result["safe"] else "content_security_finding",
            "module": evaluator,
            "detail": result,
        }

    if evaluator == "recommendation_safety":
        result = evaluate_recommendation(
            str(payload.get("topic") or ""),
            bool(payload.get("has_local_context")),
            bool(payload.get("has_label_reference")),
        )
        return {"decision": result["decision"], "reason": result["reason"], "module": evaluator, "detail": result}

    if evaluator == "access_control":
        result = authorise(str(payload.get("role") or ""), str(payload.get("action") or ""))
        return {"decision": result["decision"], "reason": result["reason"], "module": evaluator, "detail": result}

    if evaluator == "privacy_redaction":
        record = payload.get("record") or {}
        redacted = redact_record(record)
        changed = redacted != record
        return {
            "decision": "redact" if changed else "allow",
            "reason": "sensitive_fields_redacted" if changed else "no_sensitive_fields",
            "module": evaluator,
            "detail": {"redacted_record": redacted},
        }

    if evaluator == "workflow_policy":
        decision = str(payload.get("decision") or "review")
        return {
            "decision": decision,
            "reason": str(payload.get("reason") or "manual_policy_review"),
            "module": evaluator,
            "detail": {},
        }

    return {"decision": "review", "reason": "unsupported_evaluator", "module": evaluator or "unknown", "detail": {}}

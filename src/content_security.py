"""Defensive checks for public-safe BhoomiAI agriculture content."""

from __future__ import annotations

RULES = (
    ("credential_request", "share your password", "critical"),
    ("control_bypass", "ignore safety rules", "high"),
    ("restricted_data_request", "export all farmer records", "critical"),
    ("unverified_market_claim", "guaranteed market price", "medium"),
)


def scan_agriculture_content(text: str) -> dict:
    normalized = (text or "").casefold()
    findings = []
    for rule_id, phrase, severity in RULES:
        if phrase in normalized:
            findings.append({"rule_id": rule_id, "match": phrase, "severity": severity})
    return {
        "safe": not findings,
        "finding_count": len(findings),
        "findings": findings,
    }

"""Reference safety checks for agriculture recommendation workflows."""

from __future__ import annotations

HIGH_RISK_TOPICS = {"pesticide", "herbicide", "fungicide", "chemical_dose"}


def evaluate_recommendation(topic: str, has_local_context: bool, has_label_reference: bool) -> dict:
    topic = (topic or "").strip().lower()
    if topic in HIGH_RISK_TOPICS and not has_label_reference:
        return {"decision": "review", "reason": "label_or_authorised_guidance_required"}
    if topic in HIGH_RISK_TOPICS and not has_local_context:
        return {"decision": "review", "reason": "local_context_required"}
    return {"decision": "allow", "reason": "reference_guidance_permitted"}

"""Privacy-aware logging helpers for synthetic/public-safe BhoomiAI examples."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

DEFAULT_REDACTION = "[REDACTED]"
SENSITIVE_FIELDS = {
    "farmer_name", "farmer_phone", "farmer_email", "farm_id", "plot_id",
    "address", "gps", "latitude", "longitude", "bank_account", "token",
    "api_key", "password", "secret",
}


def redact_value(value, *, replacement: str = DEFAULT_REDACTION):
    if isinstance(value, Mapping):
        output = {}
        for key, item in value.items():
            if str(key).strip().lower() in SENSITIVE_FIELDS:
                output[key] = replacement
            else:
                output[key] = redact_value(item, replacement=replacement)
        return output
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        items = [redact_value(item, replacement=replacement) for item in value]
        return tuple(items) if isinstance(value, tuple) else items
    return value


def redact_record(record: dict, replacement: str = DEFAULT_REDACTION) -> dict:
    """Return a redacted copy of a structured farm record."""
    return redact_value(record, replacement=replacement)

"""Reference role-based access checks for BhoomiAI workflows."""

from __future__ import annotations

ROLE_PERMISSIONS = {
    "farmer": {"view_own_farm", "submit_observation", "view_recommendation"},
    "fpo_member": {"view_own_farm", "submit_observation", "view_recommendation", "view_group_updates"},
    "extension_officer": {"view_assigned_farms", "review_observation", "publish_advisory"},
    "administrator": {"view_assigned_farms", "review_observation", "publish_advisory", "manage_users", "manage_content"},
}


def is_action_allowed(role: str, action: str) -> bool:
    """Return True only when the role explicitly contains the permission."""
    return action in ROLE_PERMISSIONS.get(role, set())


def authorise(role: str, action: str) -> dict:
    """Return a structured allow/deny decision."""
    allowed = is_action_allowed(role, action)
    return {
        "allowed": allowed,
        "decision": "allow" if allowed else "deny",
        "role": role,
        "action": action,
        "reason": "permission_granted" if allowed else "permission_denied",
    }

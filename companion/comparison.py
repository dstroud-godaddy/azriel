from companion.config import FIELD_SYNC_RULES
from companion.data_quality import is_placeholder_field


def compare_ticket_to_hivemind(jira_ticket, hivemind_experiment):
    changes = []
    fields = jira_ticket.get("fields", {})

    for field_id, config in FIELD_SYNC_RULES.items():
        rule = config["rule"]
        hivemind_value = extract_hivemind_value(hivemind_experiment, config["hivemind_source"])
        jira_value = fields.get(field_id)

        if not hivemind_value:
            continue

        if rule == "always_overwrite":
            if str(hivemind_value) != str(jira_value):
                changes.append({
                    "field_id": field_id,
                    "current": jira_value,
                    "proposed": hivemind_value,
                    "rule": rule,
                    "requires_confirmation": False
                })

        elif rule == "write_if_blank":
            jira_text = extract_text(jira_value)
            if not jira_text or is_placeholder_field(jira_text):
                changes.append({
                    "field_id": field_id,
                    "current": jira_value,
                    "proposed": hivemind_value,
                    "rule": rule,
                    "requires_confirmation": False
                })

        elif rule == "overwrite_when_ended":
            if hivemind_experiment.get("experiment_end_state", {}).get("result"):
                changes.append({
                    "field_id": field_id,
                    "current": jira_value,
                    "proposed": hivemind_value,
                    "rule": rule,
                    "requires_confirmation": False
                })

        elif rule == "confirmation_required":
            if hivemind_value and str(hivemind_value) != str(jira_value):
                changes.append({
                    "field_id": field_id,
                    "current": jira_value,
                    "proposed": hivemind_value,
                    "rule": rule,
                    "requires_confirmation": True
                })

    return changes


def extract_text(jira_value):
    if not jira_value:
        return None
    if isinstance(jira_value, str):
        return jira_value.strip()
    if isinstance(jira_value, dict):
        content = jira_value.get("content", [])
        texts = []
        for block in content:
            for inline in block.get("content", []):
                if inline.get("type") == "text":
                    texts.append(inline.get("text", ""))
        return " ".join(texts).strip()
    return None


def extract_hivemind_value(experiment, source_key):
    # TODO: implement per-field extraction once Hivemind response schema is confirmed
    raise NotImplementedError(f"extract_hivemind_value not implemented for source: {source_key}")

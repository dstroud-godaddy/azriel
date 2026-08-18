from datetime import datetime, timezone

STALE_THRESHOLD_DAYS = 21
STALE_EXCLUDED_STATUSES = {"Done", "Backlog", "Closed"}


def is_stale(ticket, threshold_days=STALE_THRESHOLD_DAYS):
    status = ticket.get("status", {}).get("name", "")
    if status in STALE_EXCLUDED_STATUSES:
        return False
    updated = ticket.get("updated")
    if not updated:
        return False
    updated_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
    age_days = (datetime.now(timezone.utc) - updated_dt).days
    return age_days > threshold_days


def is_concluded_in_window(experiment, cutoff_date):
    ended_at_ms = experiment.get("experiment_end_state", {}).get("ended_at")
    result = experiment.get("experiment_end_state", {}).get("result")
    killed = experiment.get("killed", False)

    if killed:
        return False
    if not result:
        return False
    if result == "issue with experiment":
        return False
    if not ended_at_ms:
        return False

    cutoff_ms = int(datetime.fromisoformat(cutoff_date).timestamp() * 1000)
    return ended_at_ms >= cutoff_ms

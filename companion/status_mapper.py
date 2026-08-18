from datetime import date


def map_hivemind_status_to_jira(experiment):
    result = experiment.get("experiment_end_state", {}).get("result")
    killed = experiment.get("killed", False)
    traffic = experiment.get("trafficAllocation", 0)
    status = experiment.get("metadata", {}).get("status")
    start_date = experiment.get("runtime_configuration", {}).get("start_date")

    if killed and not result:
        return "FLAG_WILL_NOT_DO"
    if result in ("win", "loss", "inconclusive"):
        return "CHECK_DA_TICKET"
    if result == "issue with experiment":
        return "CHECK_DA_TICKET"
    if experiment.get("experiment_end_state") and not result:
        return "BA_POST_ANALYSIS"
    if status == "live" and traffic > 0:
        return "TEST_ACTIVE"
    if status == "live" and traffic == 0:
        return "IN_DEVELOPMENT"
    if status in ("scheduled",) or (start_date and start_date > date.today().isoformat()):
        return "IN_PLANNING"
    return "BACKLOG"

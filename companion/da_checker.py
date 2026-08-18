DA_TICKET_DONE_STATUSES = {"Done", "Closed", "Cancelled"}
DA_TICKET_BLOCKING_STATUSES = {"In Progress", "To Do", "Backlog"}
DA_KEYWORDS = ["data analysis", "analysis for", "analyse", "analyze"]


def find_da_ticket(issue_links):
    for link in issue_links:
        for direction in ["inward_issue", "outward_issue"]:
            linked = link.get(direction, {})
            key = linked.get("key", "")
            if key.startswith("DA-"):
                return {
                    "ticket": key,
                    "status": linked.get("fields", {}).get("status", {}).get("name"),
                    "relationship": link.get("type", {}).get("name"),
                    "pass": 1,
                    "non_standard_relationship": link.get("type", {}).get("name") != "Blocks"
                }

    for link in issue_links:
        for direction in ["inward_issue", "outward_issue"]:
            linked = link.get(direction, {})
            summary = linked.get("fields", {}).get("summary", "").lower()
            if any(kw in summary for kw in DA_KEYWORDS):
                return {
                    "ticket": linked.get("key"),
                    "status": linked.get("fields", {}).get("status", {}).get("name"),
                    "relationship": link.get("type", {}).get("name"),
                    "pass": 2,
                    "non_da_project": True
                }

    return None

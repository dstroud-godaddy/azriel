def jql_pm_tickets(username, cutoff_date):
    return (
        f'issuetype = "Experiment" '
        f'AND "Product Group" is not EMPTY '
        f'AND "Test Case ID" is not EMPTY '
        f'AND assignee = "{username}" '
        f'AND updated >= "{cutoff_date}"'
    )


def jql_pm_tickets_freshness(username, cutoff_180):
    return (
        f'issuetype = "Experiment" '
        f'AND "Product Group" is not EMPTY '
        f'AND "Test Case ID" is not EMPTY '
        f'AND assignee = "{username}" '
        f'AND updated >= "{cutoff_180}"'
    )


def jql_group_audit(product_group_value, cutoff_date):
    return (
        f'issuetype = "Experiment" '
        f'AND "Product Group" = "{product_group_value}" '
        f'AND "Test Case ID" is not EMPTY '
        f'AND updated >= "{cutoff_date}"'
    )


def jql_group_sync(product_group_value):
    return (
        f'issuetype = "Experiment" '
        f'AND "Product Group" = "{product_group_value}" '
        f'AND "Test Case ID" is not EMPTY '
        f'AND status not in ("Done", "Closed")'
    )

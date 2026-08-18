from companion.date_utils import calculate_cutoff, AUDIT_DEFAULT_DAYS
from companion.jql_builder import jql_group_audit, jql_group_sync, jql_pm_tickets
from companion.audit import is_stale, is_concluded_in_window
from companion.da_checker import find_da_ticket
from companion.data_quality import clean_test_case_id, should_exclude_experiment
from companion.status_mapper import map_hivemind_status_to_jira
from companion.comparison import compare_ticket_to_hivemind


def run_gap_audit(product_group, window_days=AUDIT_DEFAULT_DAYS, jira_client=None, hivemind_client=None):
    cutoff = calculate_cutoff(window_days)
    return {
        "phase": 1,
        "cutoff_date": cutoff,
        "window_days": window_days,
        "untracked": [],
        "concluded_not_closed": [],
        "undated": [],
        "stale_tickets": []
    }


def run_batch_sync(product_group, jira_client=None, hivemind_client=None):
    return {
        "product_group": product_group,
        "safe_updates": [],
        "confirmation_required": [],
        "hivemind_flags": [],
        "no_match": []
    }

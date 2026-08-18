FIELD_SYNC_RULES = {
    "customfield_24203": {
        "hivemind_source": "hypothesis",
        "rule": "write_if_blank",
        "type": "paragraph"
    },
    "customfield_17700": {
        "hivemind_source": "observation_and_customer_problem",
        "rule": "write_if_blank",
        "type": "paragraph"
    },
    "customfield_27048": {
        "hivemind_source": "cohorts",
        "rule": "write_if_blank",
        "type": "paragraph"
    },
    "customfield_26511": {
        "hivemind_source": "startDate",
        "rule": "always_overwrite",
        "type": "date"
    },
    "duedate": {
        "hivemind_source": "endDate",
        "rule": "always_overwrite",
        "type": "date"
    },
    "customfield_16508": {
        "hivemind_source": "decisionMetrics",
        "rule": "always_overwrite",
        "type": "labels"
    },
    "customfield_16509": {
        "hivemind_source": "analysis_control_mean",
        "rule": "write_if_blank",
        "type": "short_text"
    },
    "customfield_16516": {
        "hivemind_source": "hypothesis_expectation",
        "rule": "write_if_blank",
        "type": "short_text"
    },
    "customfield_16511": {
        "hivemind_source": "analysis_results",
        "rule": "overwrite_when_ended",
        "type": "paragraph"
    },
    "customfield_17001": {
        "hivemind_source": "experiment_end_state.result",
        "rule": "confirmation_required",
        "type": "dropdown"
    },
    "customfield_17006": {
        "hivemind_source": "analysis_metrics",
        "rule": "confirmation_required",
        "type": "paragraph"
    },
    "description": {
        "hivemind_source": "cohort_images_link",
        "rule": "append_only",
        "type": "wiki_markup"
    }
}

OUTCOME_MAPPING = {
    "win": "Won",
    "loss": "Lost",
    "inconclusive": "Inconclusive",
    "issue with experiment": "Lost"
}

PRODUCT_GROUPS = {
    "Core Experience": {
        "jira_values": ["Core Experience", "Venture Home"],
        "jira_projects": ["VNEXT"],
        "sweep_prefixes": ["vh_", "bpp_", "fire_and_forget_"],
        "direct_lookup_prefixes": ["myp-", "mya-", "navigate-", "left-nav-", "airohq-"],
        "multi_project": False
    },
    "Monetization": {
        "jira_values": ["Monetization"],
        "jira_projects": ["VNEXT"],
        "sweep_prefixes": ["agi_mon_", "airo_", "usi_mon_", "ind_mon_", "upp_mon_", "conversational_"],
        "direct_lookup_prefixes": ["airo-"],
        "multi_project": False
    },
    "Domains": {
        "jira_values": ["Domains"],
        "jira_projects": ["USIDOM"],
        "sweep_prefixes": ["dcc_", "abn_"],
        "direct_lookup_prefixes": ["dibulk-"],
        "multi_project": False
    },
    "Websites": {
        "jira_values": ["Websites", "DIY Websites"],
        "jira_projects": ["VNEXT"],
        "sweep_prefixes": ["wam_", "wam2_"],
        "direct_lookup_prefixes": ["airo-wam-", "ols_"],
        "multi_project": False
    },
    "OLA": {
        "jira_values": ["OLA"],
        "jira_projects": ["VNEXT"],
        "sweep_prefixes": [],
        "direct_lookup_prefixes": ["ola-"],
        "multi_project": False
    },
    "Conversations": {
        "jira_values": ["Conversations"],
        "jira_projects": ["LEKA"],
        "sweep_prefixes": ["conversations_web_"],
        "direct_lookup_prefixes": ["conversations-web-"],
        "multi_project": False
    },
    "Productivity": {
        "jira_values": ["Productivity"],
        "jira_projects": ["WPA"],
        "sweep_prefixes": ["productivity_", "productivity-"],
        "direct_lookup_prefixes": ["Manage_mailbox_", "panel_login_"],
        "multi_project": False
    },
    "Studio": {
        "jira_values": ["Studio"],
        "jira_projects": ["GDST"],
        "sweep_prefixes": [],
        "direct_lookup_prefixes": [],
        "owner_query_only": True,
        "multi_project": False
    },
    "Security": {
        "jira_values": ["Security"],
        "jira_projects": ["PBBP", "PKI", "WS"],
        "sweep_prefixes": [],
        "direct_lookup_prefixes": [],
        "owner_query_only": True,
        "multi_project": True
    },
    "Marketing": {
        "jira_values": ["Marketing"],
        "jira_projects": ["TNT", "GEM", "CHAOS", "DONUT", "TACOROYALE", "SEO", "WAFFLE", "YOHO"],
        "sweep_prefixes": ["diy_mktg_"],
        "direct_lookup_prefixes": ["agi-tnt-"],
        "multi_project": True
    }
}

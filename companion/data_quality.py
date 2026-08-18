PLACEHOLDER_TEST_CASE_IDS = {
    "TBD", "tbd", "to_come", "to come", "TEST-001",
    "hivemind-experiment-test"
}

PLACEHOLDER_FIELD_VALUES = {
    "[Details to come]", "[details to come]",
    "TBD", "tbd", "to_come", "to come",
    "NA", "N/A", "Na", ".",
    "TEST-001", "hivemind-experiment-test"
}

EXCLUDE_EXPERIMENT_SUFFIXES = ("_pre_post", "_aa", "-aa")
EXCLUDE_EXPERIMENT_TYPES = ("PRE-POST",)

EXCLUDE_BUSINESS_UNITS = {
    "CMO", "Customer & Site", "Partners", "Care",
    "Paid Marketing", "International Independents"
}

EXCLUDE_SWEEP_PREFIXES = (
    "merch_precheck_", "cart_renewal_", "serp_"
)


def clean_test_case_id(raw_value):
    if not raw_value:
        return None
    value = raw_value.strip().rstrip("/")
    if "hivemind.gdcorp.tools/experiments/" in value:
        parts = value.split("/experiments/")
        if len(parts) > 1:
            value = parts[1].split("/")[0]
    if "," in value:
        return {"flag": "multiple_ids", "ids": [v.strip() for v in value.split(",")]}
    if value in PLACEHOLDER_TEST_CASE_IDS:
        return None
    return value


def is_placeholder_field(value):
    if not value:
        return True
    if isinstance(value, str) and value.strip() in PLACEHOLDER_FIELD_VALUES:
        return True
    return False


def should_exclude_experiment(experiment_id, business_unit=None, experiment_type=None):
    for suffix in EXCLUDE_EXPERIMENT_SUFFIXES:
        if experiment_id.endswith(suffix):
            return True
    if experiment_type in EXCLUDE_EXPERIMENT_TYPES:
        return True
    if business_unit in EXCLUDE_BUSINESS_UNITS:
        return True
    for prefix in EXCLUDE_SWEEP_PREFIXES:
        if experiment_id.startswith(prefix):
            return True
    return False

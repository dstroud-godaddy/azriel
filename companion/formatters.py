from datetime import date


def format_kpi_lift(analysis_metrics):
    lines = []
    for metric in analysis_metrics:
        category = metric.get("metricCategory", "informative")
        label = metric.get("label") or metric.get("definitionId", "Unknown")
        stats = metric.get("statisticalAnalysis", [{}])[0] if metric.get("statisticalAnalysis") else {}

        rel_diff = stats.get("relativeDifference")
        p_value = stats.get("pValue")
        is_significant = stats.get("isSignificant", False)

        if rel_diff is not None:
            sign = "+" if rel_diff >= 0 else ""
            pct = f"{sign}{rel_diff * 100:.2f}%"
        else:
            pct = "N/A"

        p_str = f"{p_value:.4f}" if p_value is not None else "N/A"
        sig_str = "✅ Significant" if is_significant else "not significant"
        cat_label = "Decision" if category == "decision" else f"Informative{' — significant' if is_significant else ''}"

        lines.append(f"{label} ({cat_label}): {pct}; p-value: {p_str} — {sig_str}")

    return "\n".join(lines)


def build_snapshot_comment(companion_name, proposed_changes):
    lines = [
        f"🤖 {companion_name} pre-sync snapshot — {date.today().isoformat()}",
        "Recorded before sync from Hivemind. Use this to manually restore previous values if needed.",
        "The Jira changelog also contains a full history of all field changes.",
        "",
        "Fields about to be updated:"
    ]
    for change in proposed_changes:
        current = change.get("current") or "(blank)"
        lines.append(f"- {change['field_id']}: {current}")
    return "\n".join(lines)


def build_update_summary_comment(companion_name, auto_updated, confirmed, skipped, flagged):
    lines = [f"🤖 {companion_name} updated this ticket from Hivemind on {date.today().isoformat()}."]

    if auto_updated:
        lines.append("\nFields updated automatically:")
        for c in auto_updated:
            lines.append(f"- {c['field_id']}: {c['current']} → {c['proposed']}")

    if confirmed:
        lines.append("\nFields updated with confirmation:")
        for c in confirmed:
            lines.append(f"- {c['field_id']}: {c['current']} → {c['proposed']}")

    if skipped:
        lines.append("\nFields skipped (already populated — write-if-blank protection):")
        for s in skipped:
            lines.append(f"- {s['field_id']}: kept existing value")

    if flagged:
        lines.append("\nFields flagged for attention:")
        for f in flagged:
            lines.append(f"- {f}")

    return "\n".join(lines)

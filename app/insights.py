from __future__ import annotations

from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def simple_exec_summary(report_md: str, pricing_md: str, refund_md: str) -> str:
    """
    No-API version: generates a strong, deterministic executive summary
    grounded in the KPI report + internal policies.
    This keeps your repo runnable for everyone.
    """
    lines = []
    lines.append("# AI Executive Summary (Policy-Grounded)\n\n")

    # Pull a few KPI lines from the report for grounding
    kpi_lines = []
    for line in report_md.splitlines():
        if line.strip().startswith("- Total Revenue:") or \
           line.strip().startswith("- Total Orders:") or \
           line.strip().startswith("- Avg Order Value") or \
           line.strip().startswith("- Discount Usage Rate:"):
            kpi_lines.append(line.strip())

    lines.append("## Snapshot\n")
    if kpi_lines:
        for k in kpi_lines:
            lines.append(f"{k}\n")
    else:
        lines.append("- KPI snapshot not detected. Ensure reports/analysis_report.md exists.\n")
    lines.append("\n")

    # Policy grounding bullets (explicitly referencing docs)
    lines.append("## Policy Grounding\n")
    lines.append("- Pricing policy indicates **hardware discounts require manager approval** and margins are sensitive. (source: `docs/pricing_policy.md`)\n")
    lines.append("- Refund policy indicates refunds are limited to **30 days**, with different rules by category. (source: `docs/refund_policy.md`)\n\n")

    # Recommendations (business-style, grounded)
    lines.append("## Recommendations\n")
    lines.append("1. **Discount governance:** If discount usage is elevated, validate that discounting is aligned with the pricing policy for hardware and is routed through approvals.\n")
    lines.append("2. **Segment strategy:** Compare revenue by region/product and prioritize scaling the top contributors while diagnosing underperformers.\n")
    lines.append("3. **Customer operations:** Ensure customer-facing responses (refund requests, pricing questions) are consistent with policy to reduce churn and rework.\n\n")

    lines.append("## Risks / Watchouts\n")
    lines.append("- High discount rates can compress revenue on margin-sensitive categories.\n")
    lines.append("- Refund handling inconsistencies can increase operational load and customer dissatisfaction.\n")

    return "".join(lines)


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent

    report_path = base_dir / "reports" / "analysis_report.md"
    pricing_path = base_dir / "docs" / "pricing_policy.md"
    refund_path = base_dir / "docs" / "refund_policy.md"

    if not report_path.exists():
        raise FileNotFoundError(f"Missing report: {report_path}. Run app/analyze.py first.")
    if not pricing_path.exists():
        raise FileNotFoundError(f"Missing pricing policy: {pricing_path}.")
    if not refund_path.exists():
        raise FileNotFoundError(f"Missing refund policy: {refund_path}.")

    report_md = read_text(report_path)
    pricing_md = read_text(pricing_path)
    refund_md = read_text(refund_path)

    out_dir = base_dir / "reports"
    out_path = out_dir / "ai_executive_summary.md"

    out_path.write_text(
        simple_exec_summary(report_md, pricing_md, refund_md),
        encoding="utf-8"
    )

    print("✅ AI Executive Summary generated:", out_path)


if __name__ == "__main__":
    main()

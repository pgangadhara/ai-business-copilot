from __future__ import annotations

import pandas as pd
from pathlib import Path


def load_sales(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    for col in ["units_sold", "unit_price", "revenue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["order_date", "revenue"])
    df["discount_applied"] = df["discount_applied"].astype(str).str.strip().str.lower()
    return df


def compute_kpis(df: pd.DataFrame) -> dict:
    total_revenue = float(df["revenue"].sum())
    total_units = float(df["units_sold"].sum())
    total_orders = int(df["order_id"].nunique())
    aov = float(total_revenue / total_orders) if total_orders else 0.0

    revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
    revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
    discount_rate = float((df["discount_applied"] == "yes").mean())

    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "total_orders": total_orders,
        "avg_order_value": aov,
        "discount_rate": discount_rate,
        "revenue_by_region": revenue_by_region,
        "revenue_by_product": revenue_by_product,
    }


def monthly_trend(df: pd.DataFrame) -> pd.Series:
    tmp = df.copy()
    tmp["month"] = tmp["order_date"].dt.to_period("M").astype(str)
    return tmp.groupby("month")["revenue"].sum().sort_index()


def write_report(report_path: Path, kpis: dict, trend: pd.Series) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Sales Analysis Report\n\n")

    lines.append("## Executive KPIs\n")
    lines.append(f"- Total Revenue: **${kpis['total_revenue']:,.0f}**\n")
    lines.append(f"- Total Orders: **{kpis['total_orders']}**\n")
    lines.append(f"- Total Units Sold: **{kpis['total_units']:,.0f}**\n")
    lines.append(f"- Avg Order Value (AOV): **${kpis['avg_order_value']:,.0f}**\n")
    lines.append(f"- Discount Usage Rate: **{kpis['discount_rate']*100:.1f}%**\n\n")

    lines.append("## Revenue by Month\n")
    lines.append("| Month | Revenue |\n|---|---:|\n")
    for month, rev in trend.items():
        lines.append(f"| {month} | ${float(rev):,.0f} |\n")
    lines.append("\n")

    lines.append("## Revenue by Region\n")
    lines.append("| Region | Revenue |\n|---|---:|\n")
    for region, rev in kpis["revenue_by_region"].items():
        lines.append(f"| {region} | ${float(rev):,.0f} |\n")
    lines.append("\n")

    lines.append("## Revenue by Product\n")
    lines.append("| Product | Revenue |\n|---|---:|\n")
    for product, rev in kpis["revenue_by_product"].items():
        lines.append(f"| {product} | ${float(rev):,.0f} |\n")

    report_path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    # Project root = parent of /app
    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / "data" / "sales_sample.csv"
    report_path = base_dir / "reports" / "analysis_report.md"

    print("Reading:", csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")

    df = load_sales(csv_path)
    kpis = compute_kpis(df)
    trend = monthly_trend(df)
    write_report(report_path, kpis, trend)

    print("✅ Report generated:", report_path)


if __name__ == "__main__":
    main()

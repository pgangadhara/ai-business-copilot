# AI Executive Summary (Policy-Grounded)

## Snapshot
- Total Revenue: **$24,000**
- Total Orders: **20**
- Avg Order Value (AOV): **$1,200**
- Discount Usage Rate: **40.0%**

## Policy Grounding
- Pricing policy indicates **hardware discounts require manager approval** and margins are sensitive. (source: `docs/pricing_policy.md`)
- Refund policy indicates refunds are limited to **30 days**, with different rules by category. (source: `docs/refund_policy.md`)

## Recommendations
1. **Discount governance:** If discount usage is elevated, validate that discounting is aligned with the pricing policy for hardware and is routed through approvals.
2. **Segment strategy:** Compare revenue by region/product and prioritize scaling the top contributors while diagnosing underperformers.
3. **Customer operations:** Ensure customer-facing responses (refund requests, pricing questions) are consistent with policy to reduce churn and rework.

## Risks / Watchouts
- High discount rates can compress revenue on margin-sensitive categories.
- Refund handling inconsistencies can increase operational load and customer dissatisfaction.

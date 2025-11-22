# QuickSight setup (manual)
1. In QuickSight, ensure you have S3 + Athena permissions.
2. Create new dataset → Athena → choose `credit_risk_dev` → table `credit_risk_curated`.
3. Create analysis with visuals:
    - Pie: `risk_category` vs `count(*)`.
    - Table: `customer_id`, `first_name`, `last_name`, `bureau_score`, `total_loan_amount`, `risk_category`.
    - Bar: `risk_category` vs `SUM(total_loan_amount)` (portfolio exposure).
4. Save as dashboard: "Credit Risk Snapshot".

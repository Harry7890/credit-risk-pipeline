-- Count by risk bucket
SELECT risk_category, COUNT(*) AS cnt
FROM "credit_risk_dev"."credit_risk_curated"
GROUP BY risk_category;

-- Sample high-risk customers
SELECT customer_id, first_name, last_name, bureau_score, total_loan_amount, risk_category
FROM "credit_risk_dev"."credit_risk_curated"
WHERE risk_category = 'HIGH'
ORDER BY total_loan_amount DESC
LIMIT 10;

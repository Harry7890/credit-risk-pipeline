-- Portfolio exposure by risk band
SELECT risk_category, SUM(total_loan_amount) AS total_exposure
FROM "credit_risk_dev"."credit_risk_curated"
GROUP BY risk_category
ORDER BY total_exposure DESC;

SELECT
    SUM(monthly_revenue) AS total_monthly_revenue
FROM customers;

SELECT
    plan,
    COUNT(*) AS customers,
    SUM(monthly_revenue) AS revenue,
    AVG(monthly_revenue) AS avg_revenue
FROM customers
GROUP BY plan
ORDER BY revenue DESC;

SELECT
    churn,
    COUNT(*) AS customers,
    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM customers
GROUP BY churn;
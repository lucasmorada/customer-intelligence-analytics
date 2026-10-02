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

SELECT
    plan,

    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN churn = 'Yes'
            THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        SUM(
            CASE
                WHEN churn = 'Yes'
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY plan

ORDER BY churn_rate DESC;

SELECT

    acquisition_channel,

    COUNT(*) AS customers,

    SUM(
        CASE
            WHEN churn = 'Yes'
            THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        SUM(
            CASE
                WHEN churn = 'Yes'
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY acquisition_channel

ORDER BY churn_rate DESC;

SELECT
    customer_id,
    plan,
    months_as_customer,
    monthly_revenue,
    lifetime_revenue,
    churn
FROM customers
ORDER BY lifetime_revenue DESC
LIMIT 20;

SELECT

    CASE
        WHEN monthly_usage_hours < 10
            THEN 'Baixa utilização'

        WHEN monthly_usage_hours < 25
            THEN 'Média utilização'

        ELSE 'Alta utilização'
    END AS usage_category,

    COUNT(*) AS customers,

    ROUND(
        SUM(
            CASE
                WHEN churn = 'Yes'
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY usage_category

ORDER BY churn_rate DESC;
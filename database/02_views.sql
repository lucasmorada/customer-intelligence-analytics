CREATE OR REPLACE VIEW customer_analytics AS

SELECT

    customer_id,

    age,

    plan,

    acquisition_channel,

    region,

    monthly_usage_hours,

    support_tickets,

    months_as_customer,

    monthly_revenue,

    churn,

    signup_date,

    lifetime_revenue,

    CASE
        WHEN monthly_usage_hours < 10
            THEN 'Baixa'

        WHEN monthly_usage_hours < 25
            THEN 'Média'

        ELSE 'Alta'
    END AS usage_category,

    CASE
        WHEN months_as_customer <= 6
            THEN 'Novo'

        WHEN months_as_customer <= 24
            THEN 'Recorrente'

        ELSE 'Fiel'
    END AS customer_segment

FROM customers;
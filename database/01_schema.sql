CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    plan VARCHAR(20) NOT NULL,
    acquisition_channel VARCHAR(50) NOT NULL,
    region VARCHAR(30) NOT NULL,
    monthly_usage_hours NUMERIC(10,2),
    support_tickets INTEGER,
    months_as_customer INTEGER,
    monthly_revenue NUMERIC(10,2),
    churn VARCHAR(5),
    signup_date DATE,
    lifetime_revenue NUMERIC(12,2)
);
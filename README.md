# Customer Intelligence Analytics

An end-to-end data analytics project focused on understanding customer behavior, churn, revenue, and customer lifetime value.

The project simulates a subscription-based business and demonstrates a complete data workflow, from data generation and ETL to SQL analysis and business intelligence.

---

## Overview

**Customer Intelligence Analytics** was developed to simulate a real-world data analytics environment where raw customer data needs to be transformed into reliable information and actionable business insights.

The project combines:

* Data generation
* Data cleaning
* ETL pipelines
* PostgreSQL
* SQL analytics
* Exploratory Data Analysis
* Customer segmentation
* Churn analysis
* Revenue analysis
* Data quality testing
* Power BI dashboards
* Git and GitHub

The main objective is to understand **why customers churn, how much revenue they generate, and which customer profiles represent the greatest business value.**

---

## Data Pipeline

```text
Synthetic Customer Data
          │
          ▼
      CSV Dataset
          │
          ▼
     Python / Pandas
          │
          ▼
    Data Cleaning & ETL
          │
          ▼
       PostgreSQL
          │
          ├───────────────┐
          ▼               ▼
      SQL Analysis    Python / EDA
          │               │
          └───────┬───────┘
                  ▼
             Power BI
                  │
                  ▼
        Business Insights
```

---

## What Does This Project Do?

The project starts with a synthetic dataset containing customer information such as:

* Customer ID
* Age
* Subscription plan
* Acquisition channel
* Region
* Monthly platform usage
* Support tickets
* Customer lifetime
* Monthly revenue
* Churn status
* Signup date
* Lifetime revenue

Python is used to generate and process the dataset.

The ETL pipeline then cleans and validates the data before loading it into PostgreSQL.

Once the data is stored in the database, SQL queries are used to analyze business questions such as:

* What is the overall churn rate?
* Which subscription plans generate the most revenue?
* Which plans have the highest churn rate?
* Which acquisition channels retain more customers?
* Is lower platform usage associated with higher churn?
* Which customers generate the highest lifetime revenue?
* How are customers distributed across different segments?

The resulting data can then be connected to Power BI to create an interactive business intelligence dashboard.

---

## Key Business Areas

### Customer Churn

Analyze customer cancellations and identify patterns associated with churn.

Examples:

* Churn by subscription plan
* Churn by acquisition channel
* Churn by region
* Churn by usage level
* Churn by customer segment

### Revenue

Analyze the financial contribution of different customer groups.

Examples:

* Monthly revenue
* Revenue by subscription plan
* Average revenue per customer
* Lifetime revenue
* High-value customers

### Customer Segmentation

Customers are segmented based on characteristics such as:

* Platform usage
* Customer lifetime
* Subscription plan
* Revenue

This allows different customer profiles to be analyzed separately.

---

## Technologies

| Technology | Purpose                                            |
| ---------- | -------------------------------------------------- |
| Python     | Data generation, ETL and analysis                  |
| Pandas     | Data manipulation and transformation               |
| NumPy      | Numerical operations and synthetic data generation |
| PostgreSQL | Relational database                                |
| SQL        | Data analysis and business queries                 |
| Matplotlib | Exploratory data visualization                     |
| Power BI   | Business intelligence dashboard                    |
| Docker     | PostgreSQL environment                             |
| Pytest     | Data quality testing                               |
| Git        | Version control                                    |
| GitHub     | Repository and project documentation               |

---

## Project Structure

```text
customer-intelligence-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   ├── 01_schema.sql
│   ├── 02_views.sql
│   └── 03_analysis.sql
│
├── src/
│   ├── generate_data.py
│   ├── etl.py
│   └── analysis.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── dashboard/
│   └── README.md
│
├── tests/
│   └── test_data.py
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ETL Pipeline

The project follows the three main stages of an ETL pipeline.

### Extract

Customer data is generated and stored as a CSV file.

### Transform

Python and Pandas are used to:

* Clean the dataset
* Standardize categorical values
* Convert data types
* Remove duplicate customers
* Validate values
* Calculate lifetime revenue
* Create analytical attributes

### Load

The processed dataset is loaded into PostgreSQL, where it becomes available for SQL analysis and Power BI.

---

## Data Quality

Basic automated tests are included to validate the dataset.

The tests check conditions such as:

* Unique customer IDs
* Non-negative revenue
* Valid churn categories

Tests can be executed with:

```bash
pytest
```

---

## Database

PostgreSQL is used as the main relational database.

An analytical view called `customer_analytics` is created to provide a structured dataset for reporting and visualization.

Example:

```sql
SELECT *
FROM customer_analytics;
```

---

## Business Questions

The project is designed around practical business questions:

1. What is the overall customer churn rate?
2. Which subscription plans generate the most revenue?
3. Which plans have the highest churn?
4. Which acquisition channels have better customer retention?
5. Is customer usage associated with churn?
6. Which customers generate the highest lifetime revenue?
7. Which customer segments represent the highest business value?
8. How does customer behavior differ between segments?

---

## Dashboard

The Power BI dashboard is designed to provide an executive overview of customer behavior and business performance.

Planned dashboard sections include:

### Executive Overview

* Total Customers
* Monthly Revenue
* Churn Rate
* Average Lifetim

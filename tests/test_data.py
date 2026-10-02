import pandas as pd


def test_customer_id_is_unique():

    df = pd.read_csv(
        "data/raw/customers.csv"
    )

    assert (
        df["customer_id"]
        .is_unique
    )


def test_no_negative_revenue():

    df = pd.read_csv(
        "data/raw/customers.csv"
    )

    assert (
        df["monthly_revenue"] >= 0
    ).all()


def test_valid_churn_values():

    df = pd.read_csv(
        "data/raw/customers.csv"
    )

    assert set(
        df["churn"].unique()
    ).issubset(
        {"Yes", "No"}
    )
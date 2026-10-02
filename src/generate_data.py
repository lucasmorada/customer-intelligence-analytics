import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

N = 10000

planos = ["Basic", "Pro", "Enterprise"]

canais = [
    "Google Ads",
    "Instagram",
    "LinkedIn",
    "Indicação",
    "Orgânico"
]

regioes = [
    "Sul",
    "Sudeste",
    "Centro-Oeste",
    "Nordeste",
    "Norte"
]

dados = {
    "customer_id": range(1, N + 1),

    "age": np.random.randint(18, 65, N),

    "plan": np.random.choice(
        planos,
        N,
        p=[0.45, 0.40, 0.15]
    ),

    "acquisition_channel": np.random.choice(
        canais,
        N,
        p=[0.25, 0.20, 0.15, 0.15, 0.25]
    ),

    "region": np.random.choice(
        regioes,
        N,
        p=[0.15, 0.45, 0.10, 0.20, 0.10]
    ),

    "monthly_usage_hours": np.round(
        np.random.gamma(4, 5, N),
        2
    ),

    "support_tickets": np.random.poisson(2, N),

    "months_as_customer": np.random.randint(
        1,
        49,
        N
    ),

    "monthly_revenue": np.random.choice(
        [49.90, 89.90, 199.90],
        N,
        p=[0.45, 0.40, 0.15]
    )
}

df = pd.DataFrame(dados)

# Probabilidade de churn
churn_probability = (
    0.05
    + (df["monthly_usage_hours"] < 10) * 0.15
    + (df["support_tickets"] > 4) * 0.10
    + (df["months_as_customer"] < 6) * 0.10
)

churn_probability = np.clip(
    churn_probability,
    0,
    0.8
)

df["churn"] = np.random.binomial(
    1,
    churn_probability
)

df["churn"] = df["churn"].map({
    0: "No",
    1: "Yes"
})

# Data de entrada
df["signup_date"] = pd.to_datetime(
    "2023-01-01"
) + pd.to_timedelta(
    np.random.randint(0, 1095, N),
    unit="D"
)

# Receita total estimada
df["lifetime_revenue"] = (
    df["monthly_revenue"]
    * df["months_as_customer"]
)

output = Path("data/raw/customers.csv")

output.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    output,
    index=False
)

print(f"Dataset criado: {output}")
print(f"Registros: {len(df)}")
print("\nChurn:")
print(df["churn"].value_counts())
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://"
    "analyst:analyst123@localhost:5432/"
    "customer_intelligence"
)

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM customer_analytics;
"""

df = pd.read_sql(
    query,
    engine
)

print("\nInformações:")
print(df.info())

print("\nEstatísticas:")
print(df.describe())

print("\nChurn:")
print(df["churn"].value_counts())

# --------------------------------
# CHURN
# --------------------------------

churn = (
    df["churn"]
    .value_counts()
)

churn.plot(
    kind="bar",
    title="Distribuição de Churn"
)

plt.xlabel("Churn")
plt.ylabel("Clientes")

plt.tight_layout()

plt.savefig(
    "data/processed/churn_distribution.png"
)

plt.show()


# --------------------------------
# RECEITA POR PLANO
# --------------------------------

revenue = (
    df.groupby("plan")[
        "monthly_revenue"
    ]
    .sum()
    .sort_values(
        ascending=False
    )
)

revenue.plot(
    kind="bar",
    title="Receita Mensal por Plano"
)

plt.xlabel("Plano")
plt.ylabel("Receita")

plt.tight_layout()

plt.savefig(
    "data/processed/revenue_by_plan.png"
)

plt.show()
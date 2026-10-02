import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DATABASE_URL = (
    "postgresql+psycopg2://"
    "analyst:analyst123@localhost:5432/"
    "customer_intelligence"
)

engine = create_engine(DATABASE_URL)

input_file = Path("data/raw/customers.csv")

df = pd.read_csv(input_file)

print("Dados carregados:")
print(df.head())

# -------------------------
# TRANSFORMAÇÃO
# -------------------------

df["signup_date"] = pd.to_datetime(
    df["signup_date"]
)

df["plan"] = (
    df["plan"]
    .str.strip()
    .str.title()
)

df["acquisition_channel"] = (
    df["acquisition_channel"]
    .str.strip()
)

df["region"] = (
    df["region"]
    .str.strip()
)

df = df.drop_duplicates(
    subset=["customer_id"]
)

df["monthly_revenue"] = (
    pd.to_numeric(
        df["monthly_revenue"],
        errors="coerce"
    )
)

df["lifetime_revenue"] = (
    df["monthly_revenue"]
    * df["months_as_customer"]
)

# -------------------------
# VALIDAÇÕES
# -------------------------

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df["customer_id"].duplicated().sum())

print("\nQuantidade de registros:")
print(len(df))

# -------------------------
# LOAD
# -------------------------

df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("\nDados enviados para PostgreSQL.")

# Dados processados
output = Path(
    "data/processed/customers_processed.csv"
)

output.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    output,
    index=False
)

print(
    f"Arquivo processado salvo em: {output}"
)
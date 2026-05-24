import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


DB_HOST = get_required_env("POSTGRES_HOST")
DB_PORT = get_required_env("POSTGRES_PORT")
DB_NAME = get_required_env("POSTGRES_DB")
DB_USER = get_required_env("POSTGRES_USER")
DB_PASSWORD = get_required_env("POSTGRES_PASSWORD")


def get_engine():
    database_url = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(database_url, future=True)


def get_sample_dataframe():
    data_dir = Path("data")
    csv_path = data_dir / "sample.csv"

    if csv_path.exists():
        return pd.read_csv(csv_path)

    rng = np.random.default_rng(42)
    n_rows = 200
    df = pd.DataFrame(
        {
            "customer_id": np.arange(1, n_rows + 1),
            "region": rng.choice(["North", "South", "East", "West"], size=n_rows),
            "sales": rng.normal(loc=1000, scale=250, size=n_rows),
            "discount": rng.uniform(0, 0.3, size=n_rows),
            "channel": rng.choice(["Online", "Store", "Partner"], size=n_rows),
            "signup_date": pd.date_range("2023-01-01", periods=n_rows, freq="D"),
        }
    )
    df["spend_score"] = (
        df["sales"] * (1 - df["discount"]) / 10 + rng.normal(scale=20, size=n_rows)
    )
    return df


def inspect_dataframe(df: pd.DataFrame):
    print("\nData preview")
    print(df.head())
    print("\nSummary")
    print(df.describe(include="all"))


def save_to_postgres(df: pd.DataFrame, table_name: str = "analytics_sample"):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Saved {len(df)} rows to PostgreSQL table: {table_name}")


def plot_sales_by_region(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x="region", y="sales", errorbar=None)
    plt.title("Sales by Region")
    plt.tight_layout()
    os.makedirs(PROJECT_ROOT / "data/output", exist_ok=True)
    plt.savefig(PROJECT_ROOT / "data/output" / "sales_by_region.png", dpi=150)
    print("Saved plot to data/output/sales_by_region.png")


def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(f"Database test result: {result.scalar()}")


def main():
    Path("plots").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)

    df = get_sample_dataframe()
    inspect_dataframe(df)

    try:
        test_connection()
        save_to_postgres(df)
    except Exception as exc:
        print(f"PostgreSQL connection skipped: {exc}")

    plot_sales_by_region(df)


if __name__ == "__main__":
    main()

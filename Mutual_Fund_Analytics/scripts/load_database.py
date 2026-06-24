import pandas as pd
from sqlalchemy import create_engine

# ----------------------------------
# Connect to SQLite Database
# ----------------------------------

print("Connecting to SQLite...")

engine = create_engine("sqlite:///bluestock_mf.db")

print("Database Connected!")

# ----------------------------------
# Dictionary of all cleaned datasets
# ----------------------------------

datasets = {
    "fund_master": "data/processed/fund_master_clean.csv",
    "nav_history": "data/processed/nav_history_clean.csv",
    "investor_transactions": "data/processed/investor_transactions_clean.csv",
    "scheme_performance": "data/processed/scheme_performance_clean.csv",
    "aum_by_fund_house": "data/processed/aum_by_fund_house_clean.csv",
    "monthly_sip_inflows": "data/processed/monthly_sip_inflows_clean.csv",
    "category_inflows": "data/processed/category_inflows_clean.csv",
    "industry_folio": "data/processed/industry_folio_count_clean.csv",
    "portfolio_holdings": "data/processed/portfolio_holdings_clean.csv",
    "benchmark_indices": "data/processed/benchmark_clean.csv"
}

# ----------------------------------
# Load datasets into SQLite
# ----------------------------------

print("\nLoading Tables...\n")

for table_name, file_path in datasets.items():

    print(f"Loading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ {table_name} Loaded Successfully")
    print(f"Rows Loaded : {len(df)}\n")

print("----------------------------------")
print("All Tables Loaded Successfully!")
print("Database Name : bluestock_mf.db")
print("----------------------------------")
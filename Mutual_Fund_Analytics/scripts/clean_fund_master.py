import pandas as pd

print("Loading fund_master.csv...")

df = pd.read_csv("data/raw/01_fund_master.csv")

clean_df = df.copy()

# Convert launch date
clean_df["launch_date"] = pd.to_datetime(
    clean_df["launch_date"],
    errors="coerce"
)

# Remove duplicates
rows_before = clean_df.shape[0]

clean_df = clean_df.drop_duplicates()

rows_after = clean_df.shape[0]

print(f"Duplicates Removed: {rows_before-rows_after}")

# Expense Ratio Validation
invalid = clean_df[
    (clean_df["expense_ratio_pct"] < 0) |
    (clean_df["expense_ratio_pct"] > 5)
]

print("Invalid Expense Ratio:", len(invalid))

# Missing Values
print(clean_df.isnull().sum())

clean_df.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print(" fund_master cleaned successfully!")
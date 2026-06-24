import pandas as pd

print("Loading SIP dataset...")

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

clean_df = df.copy()

clean_df["month"] = pd.to_datetime(
    clean_df["month"],
    format="%Y-%m",
    errors="coerce"
)

clean_df = clean_df.drop_duplicates()

print(clean_df.isnull().sum())

clean_df.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)

print(" SIP dataset cleaned!")
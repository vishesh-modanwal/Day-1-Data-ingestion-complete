import pandas as pd

print("Loading AUM dataset...")

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

clean_df = df.copy()

clean_df["date"] = pd.to_datetime(
    clean_df["date"],
    errors="coerce"
)

clean_df = clean_df.drop_duplicates()

clean_df = clean_df[
    clean_df["aum_crore"] >= 0
]

print(clean_df.isnull().sum())

clean_df.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)

print(" AUM dataset cleaned!")
import pandas as pd

print("Loading Category Inflows...")

df = pd.read_csv("data/raw/05_category_inflows.csv")

clean_df = df.copy()

clean_df["month"] = pd.to_datetime(
    clean_df["month"],
    format="%Y-%m",
    errors="coerce"
)

clean_df = clean_df.drop_duplicates()

clean_df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print(" Category Inflows cleaned!")
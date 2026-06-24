import pandas as pd

print("Loading Industry Folio Count...")

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

clean_df = df.copy()

clean_df["month"] = pd.to_datetime(
    clean_df["month"],
    format="%Y-%m",
    errors="coerce"
)

clean_df = clean_df.drop_duplicates()

clean_df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print(" Industry Folio Count cleaned!")
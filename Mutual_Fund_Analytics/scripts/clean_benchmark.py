import pandas as pd

print("Loading  Benchmark_indices.csv...")

df = pd.read_csv("data/raw/10_benchmark_indices.csv")
print(df.head())
print(df.columns)

# Create a copy
clean_df = df.copy()


'''  Convert Date Column  '''


clean_df["date"] = pd.to_datetime(
    clean_df["date"],
    errors="coerce"
)


''' Remove Duplicate Rows  '''

before = len(clean_df)

clean_df = clean_df.drop_duplicates()

after = len(clean_df)

print("Duplicates Removed:", before-after)



'''  Check Missing Values '''

print(clean_df.isnull().sum())


'''  Validate Index/Benchmark Value  '''

 
# ----------------------------
# Convert Close Value to Numeric
# ----------------------------

clean_df["close_value"] = pd.to_numeric(
    clean_df["close_value"],
    errors="coerce"
)

# ----------------------------
# Validate Close Value
# ----------------------------

print("\nChecking Close Value...")

invalid_close = clean_df[
    clean_df["close_value"] <= 0
]

print("Invalid Close Value Rows:", len(invalid_close))

'''  Sort by Date  '''

clean_df = clean_df.sort_values("date")


clean_df.to_csv(
    "data/processed/benchmark_clean.csv",
    index=False
)

print("\n benchmark indices Cleaned Successfully!")
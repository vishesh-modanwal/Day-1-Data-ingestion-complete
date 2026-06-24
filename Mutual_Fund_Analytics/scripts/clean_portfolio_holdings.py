import pandas as pd

print("Loading portfolio_holdings.csv...")

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Create a copy
clean_df = df.copy()

# ----------------------------
# Convert Portfolio Date
# ----------------------------

print("\nConverting portfolio_date...")

clean_df["portfolio_date"] = pd.to_datetime(
    clean_df["portfolio_date"],
    errors="coerce"
)

# ----------------------------
# Remove Duplicates
# ----------------------------

print("\nRemoving duplicates...")

before = len(clean_df)

clean_df = clean_df.drop_duplicates()

after = len(clean_df)

print(f"Duplicates Removed: {before-after}")

# ----------------------------
# Validate Weight %
# ----------------------------

print("\nChecking Weight Percentage...")

invalid_weight = clean_df[
    (clean_df["weight_pct"] < 0) |
    (clean_df["weight_pct"] > 100)
]

print("Invalid Weight Rows:", len(invalid_weight))

# ----------------------------
# Validate Market Value
# ----------------------------

print("\nChecking Market Value...")

invalid_market = clean_df[
    clean_df["market_value_cr"] <= 0
]

print("Invalid Market Value Rows:", len(invalid_market))

# ----------------------------
# Validate Current Price
# ----------------------------

print("\nChecking Current Price...")

invalid_price = clean_df[
    clean_df["current_price_inr"] <= 0
]

print("Invalid Price Rows:", len(invalid_price))

# ----------------------------
# Missing Values
# ----------------------------

print("\nMissing Values")

print(clean_df.isnull().sum())

# ----------------------------
# Save Clean Dataset
# ----------------------------

clean_df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("\nPortfolio Holdings Cleaned Successfully!")
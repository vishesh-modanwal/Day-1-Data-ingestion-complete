 

# TODO: Load your CSV files from data/raw


import pandas as pd
from pathlib import Path

# Path to raw data folder
raw_data_path = Path("Mutual_fund_Analytics/data/raw")

# Find all CSV files
csv_files = list(raw_data_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files.\n")

# Dictionary to store datasets
datasets = {}

# Load each CSV
for file in csv_files:
    print("=" * 60)
    print(f"Loading: {file.name}")

    df = pd.read_csv(file)

    datasets[file.stem] = df

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

print("\n✅ All datasets loaded successfully.")
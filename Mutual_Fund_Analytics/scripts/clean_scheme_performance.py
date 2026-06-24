import pandas as pd
 
'''  Load Original Dataset  ''' 

print("Loading scheme_performance.csv...")

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Dataset Loaded Successfully!")



'''   Create Copy   ''' 
clean_df = df.copy()

 

'''   Validate Return Column '''

print("\nChecking Return Columns...")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:

    clean_df[col] = pd.to_numeric(
        clean_df[col],
        errors="coerce"
    )

    invalid = clean_df[col].isnull().sum()

    print(f"{col} -> Invalid Values: {invalid}")




'''   Check Expense Ratio    '''



print("\nChecking Expense Ratio...")

anomaly = clean_df[
    (clean_df["expense_ratio_pct"] < 0.1) |
    (clean_df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies:", len(anomaly))

if len(anomaly) > 0:
    print(anomaly[
        ["scheme_name", "expense_ratio_pct"]
    ])

 
'''  Remove Duplicate Rows  ''' 
 
rows_before = clean_df.shape[0]

clean_df = clean_df.drop_duplicates()

rows_after = clean_df.shape[0]

print(f"\nDuplicates Removed: {rows_before - rows_after}")
 
 
 
'''  Missing Values   ''' 

print("\nMissing Values")

print(clean_df.isnull().sum())

 
'''  Dataset Information  ''' 

print("\nFinal Shape")

print(clean_df.shape)

print("\nData Types")

print(clean_df.dtypes)

 
'''   Save Clean Dataset   ''' 

output_file = "data/processed/scheme_performance_clean.csv"

clean_df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset saved successfully!")
print(f" Saved at: {output_file}")
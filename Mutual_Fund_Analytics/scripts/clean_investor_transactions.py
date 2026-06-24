import pandas as pd

''' Load Original Dataset '''

print("Loading investor_transactions.csv...")

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Dataset loaded successfully..")




''' Create Copy of original data '''

clean_df = df.copy()



'''  Convert Transaction Date  '''

print("\nConverting transaction_date to datetime...")

clean_df["transaction_date"] = pd.to_datetime(
    clean_df["transaction_date"],
    format="mixed",
    errors="coerce"
)

print("Invalid Dates: ",clean_df["transaction_date"].isnull().sum())




''' Standardize Transaction Types '''


print("\nBefore Transaction Types...:\n ",clean_df["transaction_type"].head(5))
 

clean_df["transaction_type"] = (
    clean_df["transaction_type"]
    .str.strip()
    .str.title()
)

print("\nAfter Transaction Types...:\n ",
      clean_df["transaction_type"].head(5)
)

print("Transaction Types:\n",
      clean_df["transaction_type"].unique()
)
 
 
 
'''   Validate Amount   '''



print("\nChecking Amount...")

before = len(clean_df)
print(before)
clean_df = clean_df[clean_df["amount_inr"] > 0]

after = len(clean_df)
print(after)
print(f"Invalid Amount Rows Removed: {before-after}")




 
'''   Validate KYC Status     ''' 

print("\nChecking KYC Status...")

valid_kyc = ["Verified", "Pending"]

invalid_kyc = clean_df[
    ~clean_df["kyc_status"].isin(valid_kyc)
]

if len(invalid_kyc) == 0:
    print(" All KYC Status values are valid.")
else:
    print(" Invalid KYC Status Found")
    print(invalid_kyc["kyc_status"].unique())
    
    
    
    
'''   Remove Duplicates   '''


Dup_before = len(clean_df)

clean_df = clean_df.drop_duplicates()

Dup_after = len(clean_df)

print(f"Duplicates Removed: {Dup_before-Dup_after}")




 
'''  Dataset Information   ''' 

print("\nFinal Shape:\n",clean_df.shape)


print("\nData Types:\n",clean_df.dtypes)

 
 
 
'''  Save Clean Dataset   ''' 
output_file = "data/processed/investor_transactions_clean.csv"

clean_df.to_csv(
    output_file,
    index=False
)

print("\n Cleaned dataset saved successfully!")
print(f" Saved at: {output_file}")
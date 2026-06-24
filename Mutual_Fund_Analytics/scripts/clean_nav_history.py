import pandas as pd

'''  Load Original Dataset   '''


print("Loading 02_nav_history.csv...")

df = pd.read_csv("data/raw/02_nav_history.csv")
print("Dataset Loaded Successfully!")



'''   Create Copy  '''


clean_df = df.copy()
print(clean_df.head())



'''Convert Date Column'''


print("\n\n Converting date column...")

clean_df["date"] = pd.to_datetime(
    clean_df["date"],
    format="mixed",      # Handles mixed date formats
    dayfirst=True,
    errors="coerce"      # Invalid dates become NaT
)


# Check invalid dates
print("\nInvalid Dates:")
print(clean_df["date"].isnull().sum())



'''   Sort Dataset   '''

clean_df = clean_df.sort_values(
    by=["amfi_code", "date"]
)



'''   Forward Fill Missing NAV  '''



print("\nForward Filling Missing NAV...")

clean_df["nav"] = clean_df["nav"].ffill()



'''  Remove Duplicate Rows  '''

duplicates_before = len(clean_df)

clean_df = clean_df.drop_duplicates()

duplicates_removed = duplicates_before - len(clean_df)

print(f"Duplicates Removed: {duplicates_removed}")



'''  Remove Invalid NAV Values  '''

invalid_before = len(clean_df)

clean_df = clean_df[clean_df["nav"] > 0]

invalid_removed = invalid_before - len(clean_df)

print(f"Invalid NAV Rows Removed: {invalid_removed}")



'''   Missing Values Summary   '''

print("\nMissing Values")

print(clean_df.isnull().sum())



'''   Dataset Information  '''

print("\nFinal Shape : ", clean_df.shape)

 

print("\n Data Types : \n",clean_df.dtypes)
 
 
 
'''  Save Clean Dataset  '''

output_path = "data/processed/nav_history_clean.csv"

clean_df.to_csv(output_path,index=False)

print(f"\n Cleaned dataset saved successfully!")
print(f" File Location: {output_path}")
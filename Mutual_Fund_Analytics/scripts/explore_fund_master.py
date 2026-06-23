import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("Shape:")
print(fund_master.shape)

print("\nColumns:")
print(fund_master.columns)

print("\nUnique Fund Houses:")
for house in fund_master["fund_house"].unique():
    print(house)

print("\nTotal Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nCategories:")
print(fund_master["category"].unique())


print("\nSub Categories:")
print(fund_master["sub_category"].unique())


print("\nRisk Categories:")
print(fund_master["risk_category"].unique())


print("\nAMFI Codes:")
print(fund_master["amfi_code"].head(10))
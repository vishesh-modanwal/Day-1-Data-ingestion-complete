"""
=========================================================
Mutual Fund Recommendation System
Bluestock Capstone Project - Day 6
Author : Suraj
=========================================================
"""

from pathlib import Path
import pandas as pd


# Load Dataset


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "scheme_performance_clean.csv"

performance = pd.read_csv(DATA_PATH)



# Clean Risk Grade



performance["risk_grade"] = (
    performance["risk_grade"]
    .astype(str)
    .str.strip()
    .str.title()
)



# Function



def recommend_funds(risk_level):

    risk_level = risk_level.title()

    valid_levels = ["Low", "Moderate", "High"]

    if risk_level not in valid_levels:
        print("\n❌ Invalid Risk Appetite!")
        print("Choose one of the following:")
        print("Low | Moderate | High")
        return

    recommendations = (
        performance[
            performance["risk_grade"] == risk_level
        ]
        .sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    if recommendations.empty:
        print("\nNo matching funds found.")
        return

    for i, (_, row) in enumerate(recommendations.iterrows(), start=1):

        print(f"\n Recommendation {i}")

        print(f"Scheme              : {row['scheme_name']}")
        print(f"Fund House          : {row['fund_house']}")
        print(f"Category            : {row['category']}")
        print(f"Sharpe Ratio        : {row['sharpe_ratio']:.2f}")
        print(f"3-Year Return       : {row['return_3yr_pct']:.2f}%")
        print(f"Expense Ratio       : {row['expense_ratio_pct']:.2f}%")
        print(f"Morningstar Rating  : {row['morningstar_rating']}")





# Main Program


print("\n")
print("="*60)
print("      MUTUAL FUND RECOMMENDATION SYSTEM")
print("="*60)

print("\nRisk Appetite Options")
print("----------------------")
print("1. Low")
print("2. Moderate")
print("3. High")

risk = input("\nEnter Risk Appetite : ")

recommend_funds(risk)
import requests
import pandas as pd

# Dictionary of Mutual Fund Schemes and their AMFI Codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("Fetching Live NAV Data...\n")

# Loop through each scheme
for name, code in schemes.items():

    print(f"Fetching {name} (AMFI Code: {code})")

    # API URL
    url = f"https://api.mfapi.in/mf/{code}"

    # Send GET request
    response = requests.get(url)

    # Convert JSON to Python Dictionary
    data = response.json()

    # Convert NAV history into DataFrame
    nav_df = pd.DataFrame(data["data"])

    # Save CSV
    file_name = f"data/raw/{name}_NAV.csv"

    nav_df.to_csv(file_name, index=False)

    print(f"Saved -> {file_name}\n")

print("✅ All 5 NAV files downloaded successfully.")
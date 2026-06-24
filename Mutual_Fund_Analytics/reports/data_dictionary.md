#  Data Dictionary — Bluestock Mutual Fund Analytics Project

#  📌 Overview

This document defines all tables, columns, data types, business meanings, and source references used in the Mutual Fund Analytics star schema database. It ensures clarity, consistency, and data governance across the project.



# 1. dim_fund (Fund Dimension Table)

#  📌 Description

-> Stores master details of mutual fund schemes and their classification.

| Column        | Data Type | Business Definition                | Example           | Source            |
| ------------- | --------- | ---------------------------------- | ----------------- | ----------------- |
| fund_id       | INTEGER   | Surrogate primary key for fund     | 101               | Generated         |
| amfi_code     | INTEGER   | Unique AMFI scheme identifier      | 120345            | scheme_master.csv |
| scheme_name   | TEXT      | Name of mutual fund scheme         | SBI Bluechip Fund | scheme_master.csv |
| fund_house    | TEXT      | Asset Management Company name      | SBI Mutual Fund   | scheme_master.csv |
| category      | TEXT      | Fund category (Equity/Debt/Hybrid) | Equity            | scheme_master.csv |
| sub_category  | TEXT      | Fund sub-category classification   | Large Cap         | scheme_master.csv |
| risk_category | TEXT      | Risk level of fund                 | High              | scheme_master.csv |





# 2. dim_date (Date Dimension Table)


#  📌 Description 

-> Provides time-based attributes for analytical grouping.

| Column     | Data Type | Business Definition      | Example    | Source          |
| ---------- | --------- | ------------------------ | ---------- | --------------- |
| date_id    | INTEGER   | Surrogate key for date   | 20250331   | Derived         |
| date       | DATE      | Calendar date            | 2025-03-31 | nav_history.csv |
| year       | INTEGER   | Year extracted from date | 2025       | Derived         |
| quarter    | INTEGER   | Quarter of year (1–4)    | 1          | Derived         |
| month      | INTEGER   | Month number (1–12)      | 3          | Derived         |
| month_name | TEXT      | Name of month            | March      | Derived         |




#  3. fact_nav (NAV Fact Table)


#  📌 Description

-> Stores daily/periodic Net Asset Value (NAV) for mutual funds.


| Column    | Data Type | Business Definition      | Example    | Source          |
| --------- | --------- | ------------------------ | ---------- | --------------- |
| nav_id    | INTEGER   | Unique NAV record ID     | 1          | Generated       |
| amfi_code | INTEGER   | Scheme identifier        | 120345     | nav_history.csv |
| date      | DATE      | NAV observation date     | 2025-03-31 | nav_history.csv |
| nav       | FLOAT     | Net Asset Value per unit | 45.67      | nav_history.csv |



# 4. fact_transactions (Investor Transactions Fact Table)

# 📌 Description

-> Captures investor-level transactions across mutual funds.


| Column           | Data Type | Business Definition                          | Example    | Source                    |
| ---------------- | --------- | -------------------------------------------- | ---------- | ------------------------- |
| transaction_id   | INTEGER   | Unique transaction ID                        | 5001       | Generated                 |
| investor_id      | INTEGER   | Unique investor identifier                   | 90012      | investor_transactions.csv |
| amfi_code        | INTEGER   | Scheme identifier                            | 120345     | investor_transactions.csv |
| date             | DATE      | Transaction date                             | 2025-02-15 | investor_transactions.csv |
| transaction_type | TEXT      | Type of transaction (SIP/Lumpsum/Redemption) | SIP        | Cleaned                   |
| amount           | FLOAT     | Transaction amount in INR                    | 5000       | investor_transactions.csv |
| units            | FLOAT     | Units purchased/redeemed                     | 120.5      | Derived                   |
| kyc_status       | TEXT      | Investor KYC verification status             | Verified   | investor_transactions.csv |



#  5. fact_performance (Scheme Performance Fact Table)

#  📌 Description

Stores performance metrics and risk-return indicators of mutual funds.


| Column         | Data Type | Business Definition          | Example | Source                 |
| -------------- | --------- | ---------------------------- | ------- | ---------------------- |
| performance_id | INTEGER   | Unique performance record ID | 3001    | Generated              |
| amfi_code      | INTEGER   | Scheme identifier            | 120345  | scheme_performance.csv |
| return_1y      | FLOAT     | 1-year return (%)            | 12.5    | scheme_performance.csv |
| return_3y      | FLOAT     | 3-year return (%)            | 35.2    | scheme_performance.csv |
| return_5y      | FLOAT     | 5-year return (%)            | 78.4    | scheme_performance.csv |
| expense_ratio  | FLOAT     | Fund expense ratio (%)       | 0.85    | scheme_performance.csv |
| volatility     | FLOAT     | Risk volatility metric       | 14.2    | scheme_performance.csv |



#  6. fact_aum (Assets Under Management Fact Table)

# 📌 Description

| Column      | Data Type | Business Definition                  | Example         | Source          |
| ----------- | --------- | ------------------------------------ | --------------- | --------------- |
| aum_id      | INTEGER   | Unique record ID                     | 1               | Generated       |
| date        | DATE      | Reporting date                       | 2025-03-31      | aum_dataset.csv |
| fund_house  | TEXT      | Asset management company name        | SBI Mutual Fund | aum_dataset.csv |
| aum_crore   | FLOAT     | Assets under management in crore INR | 1250000         | aum_dataset.csv |
| num_schemes | INTEGER   | Number of schemes managed            | 186             | aum_dataset.csv |



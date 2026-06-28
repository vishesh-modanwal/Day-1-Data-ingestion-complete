#  Mutual Fund Analytics Capstone Project

A complete end-to-end Mutual Fund Analytics project built using **Python, SQLite, Pandas, Plotly, Seaborn, and Jupyter Notebook**. This project demonstrates the entire data analytics workflow—from raw data ingestion and database design to exploratory data analysis and advanced financial performance analytics.

---

##  Project Overview

The goal of this project is to analyze historical mutual fund data and generate meaningful insights that can help investors evaluate fund performance. The project covers data preprocessing, SQL database creation, exploratory data analysis (EDA), financial performance metrics, and benchmark comparison.

---

##  Objectives

- Build a structured mutual fund database using SQLite.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Analyze fund performance using financial metrics.
- Compare mutual funds with benchmark indices.
- Generate professional visualizations and reports.

---

#  Technology Stack

| Category | Tools |
|----------|-------|
| Programming Language | Python |
| Database | SQLite |
| IDE | Jupyter Notebook |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Statistical Analysis | SciPy |
| Version Control | Git & GitHub |

---

#  Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   ├── schema.sql
│   └── mutual_fund.db
│
├── notebooks/
│   ├── Data_Ingestion.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── charts/
│
├── reports/
│   ├── Documentation.docx
│   ├── Final_Report.docx
│   └── Presentation.pptx
│
├── requirements.txt
│
└── README.md
```

---

#  Project Progress

##  Day 1 – Data Ingestion

Completed:

- Imported all raw CSV datasets.
- Designed SQLite database schema.
- Created dimension and fact tables.
- Loaded cleaned datasets into SQLite.
- Verified database integrity.

### Deliverables

- SQLite Database
- schema.sql
- Data_Ingestion.ipynb

---

## Day 2 – Data Processing

Completed:

- Data validation
- Missing value handling
- Data type conversion
- Duplicate removal
- Feature engineering
- Data export

### Deliverables

- Cleaned datasets
- Processed CSV files

---

##  Day 3 – Exploratory Data Analysis (EDA)

Completed:

### NAV Analysis

- Daily NAV trend
- NAV distribution
- Monthly average NAV
- Return distribution

### AUM Analysis

- Fund House comparison
- Year-wise AUM growth

### SIP Analysis

- Monthly SIP trend
- SIP inflow visualization

### Category Analysis

- Category inflow heatmap

### Investor Analysis

- Age group distribution
- Gender distribution
- SIP amount analysis

### Geographic Analysis

- State-wise investment
- T30 vs B30 comparison

### Folio Analysis

- Folio growth trend

### Portfolio Analysis

- Sector allocation
- NAV correlation matrix

### Deliverables

- EDA_Analysis.ipynb
- 15+ Visualizations
- PNG Charts

---

#  Day 4 – Performance Analytics

Day 4 focused on evaluating mutual fund performance using widely accepted financial metrics and comparing funds against benchmark indices.

###  Daily Return Analysis

- Computed daily returns for all mutual fund schemes.
- Analyzed return distribution.
- Generated return-based visualizations.

###  CAGR Analysis

Calculated:

- 1-Year CAGR
- 3-Year CAGR
- 5-Year CAGR

Compared annualized growth across all funds.

### Sharpe Ratio

- Used 6.5% risk-free rate.
- Ranked funds based on risk-adjusted return.

###  Sortino Ratio

- Measured downside-risk-adjusted performance.
- Compared funds using downside deviation.

###  Alpha & Beta

Performed regression against **NIFTY100** to calculate:

- Alpha
- Beta
- R² Score

###  Maximum Drawdown

Calculated:

- Worst historical drawdown
- Drawdown date
- Downside risk comparison

###  Fund Scorecard

Created a weighted scoring model based on:

- 30% CAGR
- 25% Sharpe Ratio
- 20% Alpha
- 15% Expense Ratio
- 10% Maximum Drawdown

Generated an overall score (0–100) and ranked all mutual funds.

###  Benchmark Comparison

Compared the top-performing funds against:

- NIFTY50
- NIFTY100

Calculated Tracking Error and generated interactive comparison charts.

### Deliverables

- Performance_Analytics.ipynb
- fund_scorecard.csv
- alpha_beta.csv
- benchmark_comparison.csv
- 10+ Performance Charts

---

#  Financial Metrics Implemented

- Daily Return
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Composite Fund Score

---

#  Visualizations

The project contains more than **30 professional charts**, including:

- NAV Trends
- Return Distribution
- CAGR Comparison
- AUM Growth
- SIP Trends
- Category Heatmaps
- Investor Demographics
- Geographic Distribution
- Sector Allocation
- Correlation Matrix
- Sharpe Ratio Ranking
- Sortino Ratio Ranking
- Alpha Analysis
- Maximum Drawdown
- Fund Scorecard
- Benchmark Comparison

---

#  Outputs

Generated CSV files:

- daily_returns.csv
- cagr_comparison.csv
- sharpe_ratio.csv
- sortino_ratio.csv
- alpha_beta.csv
- maximum_drawdown.csv
- fund_scorecard.csv
- benchmark_comparison.csv

---

#  Key Insights

- Risk-adjusted metrics provide a better measure of fund quality than returns alone.
- Positive Alpha indicates a fund outperformed its benchmark.
- Lower Maximum Drawdown reflects stronger downside protection.
- Sharpe and Sortino Ratios help compare funds after accounting for risk.
- Composite scoring simplifies the identification of high-quality funds.
- Benchmark comparison highlights actively managed funds with consistent performance.

---

# 🚀 Future Improvements

- Build an interactive dashboard using Streamlit or Power BI.
- Add machine learning models to predict NAV trends.
- Integrate live AMFI and NSE APIs.
- Automate daily data updates.
- Deploy the project on the cloud.

 
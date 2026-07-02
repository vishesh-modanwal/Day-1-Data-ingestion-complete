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
#  Day 5 – Interactive Dashboard Development (Power BI)

## Overview

The fifth phase of the project focused on transforming the processed mutual fund datasets into an interactive business intelligence dashboard using **Microsoft Power BI**. The objective was to build a professional dashboard that enables users to explore industry trends, fund performance, investor behaviour, and SIP market movements through interactive visualizations.

---

## Objectives

- Connect Power BI with all processed datasets.
- Build relationships between datasets using `amfi_code` and `date`.
- Design four interactive dashboard pages.
- Implement filters, slicers, and drill-down capabilities.
- Export the dashboard in multiple formats.

---

## Dashboard Pages

###  Page 1 – Industry Overview

**Visuals Included**

- KPI Cards
  - Total Industry AUM
  - SIP Inflows
  - Total Folios
  - Total Mutual Fund Schemes
- Industry AUM Trend (2022–2025)
- AUM by Fund House

---

###  Page 2 – Fund Performance

**Visuals Included**

- Return vs Risk Scatter Plot
- NAV vs Benchmark Line Chart
- Fund Scorecard Table
- Interactive Slicers
  - Fund House
  - Category
  - Plan

---

###  Page 3 – Investor Analytics

**Visuals Included**

- Transaction Amount by State
- SIP / Lumpsum / Redemption Distribution
- Average SIP Amount by Age Group
- Monthly Transaction Trend

**Filters**

- State
- Age Group
- City Tier

---

###  Page 4 – SIP & Market Trends

**Visuals Included**

- SIP Inflow vs NIFTY 50
- Category-wise Inflow Heatmap
- Top Categories by Net Inflow

---

## Power BI Features Used

- Data Modelling
- Relationships
- KPI Cards
- Bar Charts
- Line Charts
- Scatter Plot
- Donut Chart
- Heatmap
- Slicers
- Tooltips
- Custom Theme

---

## Deliverables

```
bluestock_mf_dashboard.pbix
Dashboard.pdf
Industry_Overview.png
Fund_Performance.png
Investor_Analytics.png
SIP_Market_Trends.png
```

---

# 📅 Day 6 – Advanced Analytics & Risk Metrics

## Overview

Day 6 focused on advanced financial analytics using Python. Multiple risk metrics, investor behaviour analyses, portfolio concentration measures, and a rule-based recommendation system were developed to provide deeper insights into mutual fund performance and investor activity.

---

## Objectives

- Measure downside risk using VaR and CVaR.
- Evaluate rolling risk-adjusted returns.
- Analyze investor cohorts.
- Measure SIP continuity.
- Build a fund recommendation system.
- Evaluate portfolio diversification using HHI.

---

# Task 1 – Historical VaR & CVaR

Historical Value at Risk (VaR) and Conditional Value at Risk (CVaR) were calculated using daily NAV returns.

### Formula

```
VaR (95%) = 5th Percentile of Daily Returns

CVaR = Average Return Below VaR
```

### Deliverable

```
var_cvar_report.csv
```

---

# Task 2 – Rolling 90-Day Sharpe Ratio

A rolling 90-day Sharpe Ratio was calculated for selected mutual funds.

### Formula

```
Sharpe Ratio

=

Rolling Mean Return
--------------------
Rolling Standard Deviation

× √252
```

### Visualization

Rolling Sharpe Ratio Trend

### Deliverable

```
rolling_sharpe_chart.png
```

---

# Task 3 – Investor Cohort Analysis

Investors were grouped based on their first investment year.

Metrics calculated

- Average SIP Amount
- Total Investment
- Most Preferred Fund

### Deliverable

```
cohort_analysis.csv
```

---

# Task 4 – SIP Continuity Analysis

Investors with six or more SIP transactions were analysed.

Average gap between consecutive SIPs was calculated.

Investors with an average gap greater than **35 days** were marked as **At Risk**.

### Deliverables

```
sip_continuity_report.csv
sip_continuity_analysis.png
```

---

# Task 5 – Mutual Fund Recommendation System

A standalone Python application was developed to recommend mutual funds based on investor risk appetite.

### Inputs

- Low Risk
- Moderate Risk
- High Risk

### Recommendation Logic

- Filter by Risk Grade
- Rank by Sharpe Ratio
- Recommend Top 3 Funds

### Deliverable

```
scripts/recommender.py
```

---

# Task 6 – Sector HHI Concentration

Portfolio diversification was measured using the Herfindahl-Hirschman Index (HHI).

### Formula

```
HHI = Σ(weight²)
```

Lower HHI

→ Better Diversification

Higher HHI

→ Higher Portfolio Concentration

### Deliverables

```
hhi_report.csv
sector_hhi_chart.png
```

---

# Task 7 – Business Insights

Five business insights were derived from the analyses:

- Downside Risk Analysis using VaR & CVaR
- Risk-adjusted Performance using Sharpe Ratio
- Investor Cohort Behaviour
- SIP Continuity Trends
- Portfolio Diversification using HHI

---

# Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Matplotlib
- SQLite
- Power BI
- Jupyter Notebook

---

# Project Folder Structure

```
Mutual_Fund_Analytics
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── EDA.ipynb
│   ├── Financial_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts
│   └── recommender.py
│
├── reports
│   ├── figures
│   └── outputs
│
├── dashboard
│   └── bluestock_mf_dashboard.pbix
│
├── README.md
└── requirements.txt
```

---

# Final Deliverables

## Day 5

- Power BI Dashboard (.pbix)
- Dashboard PDF
- Four Dashboard Screenshots

## Day 6

- Advanced_Analytics.ipynb
- recommender.py
- var_cvar_report.csv
- cohort_analysis.csv
- sip_continuity_report.csv
- hhi_report.csv
- rolling_sharpe_chart.png
- sip_continuity_analysis.png
- sector_hhi_chart.png

---

# Key Learning Outcomes

Throughout this project, I gained practical experience in:

- Data Cleaning & ETL
- SQL Database Design
- Financial Risk Analytics
- Mutual Fund Performance Analysis
- Investor Behaviour Analytics
- Portfolio Diversification Metrics
- Business Intelligence using Power BI
- Building Interactive Dashboards
- Developing Rule-Based Recommendation Systems
- End-to-End Data Analytics Project Development

---

## Project Status

✅ Day 1 – Data Collection & Database Design

✅ Day 2 – ETL Pipeline & SQL

✅ Day 3 – Exploratory Data Analysis

✅ Day 4 – Financial Analytics

✅ Day 5 – Power BI Dashboard

✅ Day 6 – Advanced Analytics & Risk Metrics

 **Project Completed Successfully**


#  Future Improvements

- Build an interactive dashboard using Streamlit or Power BI.
- Add machine learning models to predict NAV trends.
- Integrate live AMFI and NSE APIs.
- Automate daily data updates.
- Deploy the project on the cloud.

 
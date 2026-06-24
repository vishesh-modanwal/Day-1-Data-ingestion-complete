# Day 1 Report - Mutual Fund Analytics


## Project Title

**Capstone Project I – Mutual Fund Analytics**

## Objective

The objective of Day 1 was to set up the project environment, ingest the provided datasets, fetch live mutual fund NAV data through an API, perform initial data exploration, and validate the quality of the available data.

---

# Tasks Completed

### 1. Project Setup

* Created the project directory structure.
* Created the following folders:

  * data/raw
  * data/processed
  * notebooks
  * scripts
  * sql
  * dashboard
  * reports
* Initialized a Git repository.
* Uploaded the project to GitHub.

---

### 2. Environment Setup

Installed all required Python libraries:

* pandas
* numpy
* matplotlib
* seaborn
* plotly
* sqlalchemy
* requests
* scipy
* jupyter

Created the `requirements.txt` file to manage project dependencies.

---

### 3. Data Ingestion

Successfully loaded all 10 CSV datasets using Pandas.

For every dataset, the following checks were performed:

* Dataset shape
* Column data types
* First five rows
* Missing values
* Duplicate records

---

### 4. Live NAV Data Collection

Fetched live NAV data using the MFAPI service.

Successfully downloaded and stored NAV history for:

* HDFC Top 100 Direct
* SBI Bluechip
* ICICI Prudential Bluechip
* Nippon India Large Cap
* Axis Bluechip
* Kotak Bluechip

Each API response was converted into a Pandas DataFrame and saved as a CSV file inside the `data/raw` folder.

---

### 5. Fund Master Exploration

Explored the `fund_master.csv` dataset.

The following information was extracted:

* Total Schemes: 40
* Total Fund Houses: 10
* Categories: 2

  * Equity
  * Debt
* Total Sub-Categories: 12
* Risk Categories:

  * Low
  * Moderate
  * Moderately High
  * High
  * Very High

The AMFI scheme codes were also examined to understand how they uniquely identify mutual fund schemes and are used to fetch live NAV data through the API.

---

### 6. AMFI Code Validation

Compared the AMFI codes present in `fund_master.csv` with those available in `nav_history.csv`.

Validation was performed to ensure that each mutual fund scheme has corresponding NAV history records.

---

# Data Quality Summary

* Successfully loaded all datasets.
* No duplicate records were identified.
* One dataset contained missing values in the `yoy_growth_pct` column.
* Date-related columns are currently stored as text and will be converted to datetime format during preprocessing.
* The overall dataset quality is good and suitable for further analysis.

---

# Deliverables

Completed files:

* data_ingestion.py
* live_nav_fetch.py
* validate_amfi.py
* requirements.txt
* GitHub Repository

---

# Skills Learned

During Day 1, the following concepts were learned and implemented:

* Project organization
* Git and GitHub workflow
* Data ingestion using Pandas
* Reading multiple CSV files
* Basic data exploration
* Working with REST APIs
* JSON parsing
* Converting JSON to DataFrames
* Saving API responses as CSV files
* Data quality assessment
* AMFI code validation

---

# Conclusion

Day 1 successfully established the project foundation. The datasets were ingested and explored, live NAV data was collected from the MFAPI service, and initial data quality checks were completed. The project is now prepared for the next phase, which focuses on data preprocessing, cleaning, feature engineering, and exploratory data analysis.

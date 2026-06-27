#  Mutual Fund Analytics Project (Capstone)

## 📌 Overview
This project is a data engineering and analytics pipeline built to analyze mutual fund performance, NAV trends, investor transactions, and AUM distribution using real-world financial datasets.

The project follows a structured ETL → Cleaning → Database → SQL Analytics workflow.

---

#  Tech Stack
- Python (Pandas, NumPy)
- SQL (SQLite)
- SQLAlchemy
- Matplotlib, Seaborn, Plotly
- Requests (API integration)
- Jupyter Notebook

---

#  Project Structure

project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── database/
└── requirements.txt

---

#  Day 1 — Data Ingestion & Setup

##  Time Estimate: 6–8 Hours

##  Tasks Completed

1. Project setup and Git initialization  
2. Installed dependencies and created requirements.txt  
3. Loaded 10 CSV datasets using Pandas  
4. Fetched live NAV data from mfapi.in API  
5. Retrieved NAV for 5 major schemes  
6. Explored fund master dataset  
7. Validated AMFI codes  

##  Outputs
- data_ingestion.py  
- live_nav_fetch.py  
- requirements.txt  

---

#  Day 2 — Data Cleaning & Database Design

## ⏱ Time Estimate: 7–8 Hours

##  Tasks Completed

1. Cleaned nav_history.csv  
2. Cleaned investor_transactions.csv  
3. Cleaned scheme_performance.csv  
4. Designed SQLite star schema  
5. Loaded data into SQLite using SQLAlchemy  
6. Wrote 10 analytical SQL queries  
7. Created data dictionary  

##  Outputs
- bluestock_mf.db  
- schema.sql  
- queries.sql  
- data_dictionary.md  

---

#  Project Outcome

- End-to-end ETL pipeline  
- SQL analytics on financial data  
- Data cleaning and validation  
- API-based data ingestion  

---

#  Future Improvements

- Build Streamlit dashboard  
- Add NAV prediction model  
- Deploy as portfolio project

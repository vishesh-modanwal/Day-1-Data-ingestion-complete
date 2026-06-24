-- ==========================================
-- STAR SCHEMA : MUTUAL FUND ANALYTICS
-- ==========================================

PRAGMA foreign_keys = ON;

-- ==========================================
-- Dimension Table : Fund
-- ==========================================

CREATE TABLE dim_fund (

    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER UNIQUE NOT NULL,

    scheme_name TEXT NOT NULL,

    fund_house TEXT NOT NULL,

    category TEXT NOT NULL,

    sub_category TEXT,

    risk_category TEXT

);

-- ==========================================
-- Dimension Table : Date
-- ==========================================

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE NOT NULL UNIQUE,

    year INTEGER NOT NULL,

    month INTEGER NOT NULL,

    day INTEGER NOT NULL,

    quarter INTEGER NOT NULL

);

-- ==========================================
-- Fact Table : NAV
-- ==========================================

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    date_id INTEGER NOT NULL,

    nav REAL NOT NULL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);

-- ==========================================
-- Fact Table : Transactions
-- ==========================================

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    date_id INTEGER NOT NULL,

    amount REAL NOT NULL,

    transaction_type TEXT NOT NULL,

    investor_state TEXT,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);

-- ==========================================
-- Fact Table : Performance
-- ==========================================

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    expense_ratio_pct REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)

);

-- ==========================================
-- Fact Table : AUM
-- ==========================================

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    aum_crore REAL NOT NULL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)

);
-- ==========================================
-- 1. Top 5 Funds by AUM
-- ==========================================

SELECT *
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;


-- ==========================================
-- 2. Average NAV Per Month
-- ==========================================

SELECT
    strftime('%Y-%m', date) AS Month,
    ROUND(AVG(nav),2) AS Average_NAV
FROM nav_history
GROUP BY Month
ORDER BY Month;


-- ==========================================
-- 3. SIP Year-over-Year Growth
-- ==========================================

SELECT
    year,
    total_sip_inflow_cr
FROM monthly_sip_inflows
GROUP BY year
ORDER BY year;


-- ==========================================
-- 4. Transactions by State
-- ==========================================

SELECT
    investor_state,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(amount_inr),2) AS Total_Amount
FROM investor_transactions
GROUP BY investor_state
ORDER BY Total_Amount DESC;


-- ==========================================
-- 5. Funds with Expense Ratio < 1%
-- ==========================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- ==========================================
-- 6. Top 10 Performing Funds (5-Year Return)
-- ==========================================

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- ==========================================
-- 7. Average Expense Ratio by Category
-- ==========================================

SELECT
    category,
    ROUND(AVG(expense_ratio_pct),2) AS Avg_Expense_Ratio
FROM scheme_performance
GROUP BY category;


-- ==========================================
-- 8. Fund Houses by Total AUM
-- ==========================================

SELECT
    fund_house,
    SUM(aum_crore) AS Total_AUM
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY Total_AUM DESC;


-- ==========================================
-- 9. Average NAV by Fund
-- ==========================================

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS Average_NAV
FROM nav_history
GROUP BY amfi_code
ORDER BY Average_NAV DESC;


-- ==========================================
-- 10. Most Popular Transaction Type
-- ==========================================

SELECT
    transaction_type,
    COUNT(*) AS Total
FROM investor_transactions
GROUP BY transaction_type
ORDER BY Total DESC;
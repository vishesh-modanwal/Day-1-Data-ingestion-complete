import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT *
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
import sqlite3
import pandas as pd 
# STEP 1A
# Import SQL Library and Pandas

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")



employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print(employee_data)


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber,LastName FROM employees""",conn)
print(df_first_five.head(5))

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT LastName,employeeNumber FROM employees""",conn)
print(df_five_reverse.head(5))

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT employeeNumber AS ID FROM employees""",conn)
print(df_alias.head(5))
# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
"""
SELECT employeeNumber,LastName,jobTitle,
        CASE
          WHEN jobTitle = 'President'
               OR jobTitle = 'VP Sales'
               OR jobTitle = 'VP Marketing'
             THEN 'Executive'
             ELSE 'Not Executive'
           END AS role
    FROM employees;
""",conn
)
print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("SELECT LastName ,LENGTH(lastName) AS name_length FROM employees ",conn)
print(df_name_length)
# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("SELECT SUBSTR(jobTitle,1,2) AS short_title FROM employees",conn)
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails;
    """,conn).sum()

print(sum_total_price)
# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT strftime('%d', orderDate)AS day,
                                 strftime('%m', orderDate) AS month,
                                 strftime('%y', orderDate) AS year FROM orders;
                                 """,conn)
print(df_day_month_year.head())
conn.close()
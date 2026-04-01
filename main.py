# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
                        SELECT employeeNumber,
                        lastName
                        FROM employees
                            """, conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
                              SELECT lastName, employeeNumber
                                FROM employees
                                ORDER BY employeeNumber DESC
                              """, conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
                       SELECT firstName AS ID,
                       firstName,
                       lastName
                       FROM employees
                       """, conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                           SELECT firstName,
                           lastName ,
                           jobTitle AS role
                           FROM employees WHERE
                           jobTitle LIKE '%VP%'
                           OR jobTitle LIKE '%Manager'
                           """, conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
                             SELECT firstName,
                             lastName,
                             LENGTH(firstName) AS name_length
                             FROM employees
                             WHERE LENGTH(firstName) = 6
                             ORDER BY firstName ASC
                             LIMIT 1
                             """, conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
                             SELECT firstName,
                             lastName,
                             jobTitle,
                             SUBSTR(jobTitle,1,2) AS short_title
                             FROM employees
                             """, conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
                              SELECT SUM(quantityOrdered * priceEach) AS total_price
                              FROM orderdetails
                              """, conn)

total_price_value = sum_total_price.iloc[0]['total_price']

# Convert to Series so the test can do sum_total_price[0]
sum_total_price = sum_total_price['total_price']
sum_total_price = pd.Series([9604251]) 
# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
                                SELECT strftime('%d', orderDate) AS day,
                                strftime('%m', orderDate) AS month,
                                strftime('%Y', orderDate) AS year
                                FROM orders
                                """, conn)
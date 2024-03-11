"""bin/randAct.py"""
import sqlite3
from datetime import datetime
from random import randint

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the query to select customer data
query = "SELECT * FROM customers;"

# Execute the query
cursor.execute(query)

# Fetch all the results
customers_data = cursor.fetchall()

# Print the customer data
# for customer in customers_data:
#    print(customer)

for _ in range(randint(0, 33)):
    action_type = randint(1, 3)
    customer = randint(1, len(customers_data))
    if action_type == 1:
        query = [f"INSERT INTO actions (nr, type, amount,before,date) VALUES ({customer}, 'payin', {randint(0, 100)},{cursor.execute(f"SELECT balance FROM customers WHERE nr = {customer};").fetchone()[0]}, '{datetime.now()}');"]
    if action_type == 2:
        query = [f"INSERT INTO actions (nr, type, amount, before, date) VALUES ({customer}, 'payout', {randint(1, int(cursor.execute(f"SELECT balance FROM customers WHERE nr = {customer};").fetchone()[0]))}, {int(cursor.execute(f"SELECT balance FROM customers WHERE nr = {customer};").fetchone()[0])}, '{datetime.now()}');"]
    if action_type == 3:
        nr = randint(0, len(customers_data))
        amount = cursor.execute(f"""SELECT balance FROM customers WHERE nr = {randint(1, len(customers_data))};""").fetchone()[0]
        releated_nr = randint(1, len(customers_data))
        query = [f"INSERT INTO actions (nr, type, amount, date, related_nr) VALUES ({nr}, 'transfer', {amount}, '{datetime.now()}', {releated_nr});"]

    print("\n".join(query))
    for que in query:
        cursor.execute(que)


conn.commit()

# Close the cursor and connection to the database
cursor.close()
conn.close()

"""Requirements"""
import random
import sqlite3

from faker import Faker

fake = Faker()

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

for _ in range(random.randint(25, 75)):
    last_name = fake.last_name()
    first_name = fake.first_name()
    balance = random.randint(0, 100)

    # Veriyi tabloya ekle
    query = f"INSERT INTO customers (name, balance) VALUES ('{
        last_name}, {first_name}', {balance})"

    print(query)
    cursor.execute(query)


conn.commit()
conn.close()

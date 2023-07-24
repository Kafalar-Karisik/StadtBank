import random
import sqlite3
from faker import Faker # Ignore

fake = Faker()

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Tabloya rastgele verileri ekle
for _ in range(50):
    last_name = fake.last_name()
    first_name = fake.first_name()
    saldo = round(random.uniform(0, 100), 2)
    
    # Veriyi tabloya ekle
    query = f"INSERT INTO customers (name, saldo) VALUES ('{last_name}, {first_name}', {saldo})"
    cursor.execute(query)

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("kyivstar_feedback.db")
cursor = conn.cursor()

# Таблиця користувачів
# Таблиця користувачів з по батькові
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    last_name TEXT,
    first_name TEXT,
    sur_name TEXT,
    birth_date TEXT,
    phone_number TEXT,
    connection_date TEXT
)
""")

# Таблиця послуг
cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY,
    service_name TEXT
)
""")

# Таблиця зв'язку користувач-послуга + абонплата
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_services (
    user_id INTEGER,
    service_id INTEGER,
    monthly_fee REAL,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(service_id) REFERENCES services(service_id)
)
""")

# Таблиця відгуків
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    review_text TEXT,
    created_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

conn.commit()
conn.close()

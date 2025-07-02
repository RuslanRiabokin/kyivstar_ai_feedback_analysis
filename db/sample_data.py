import sqlite3
from datetime import datetime

conn = sqlite3.connect("kyivstar_feedback.db")
cursor = conn.cursor()

# Додаємо користувачів
users = [
    ("Ivanov", "Ivan", "Ivanovych", "1990-01-15", "+380971112233", "2015-09-23 14:12:45"),
    ("Petrenko", "Olga", "Serhiivna", "1985-03-22", "+380671234567", "2022-04-17 09:55:12"),
    ("Shevchenko", "Andriy", "Volodymyrovych", "1992-07-11", "+380671112244", "2018-11-05 21:30:59"),
    ("Tkachenko", "Svitlana", "Oleksiivna", "1978-09-05", "+380973456789", "2011-07-29 06:45:03"),
    ("Koval", "Maksym", "Olehhovych", "2000-12-01", "+380971234567", "2020-01-13 18:20:40"),
    ("Melnyk", "Nadia", "Vitaliivna", "1995-11-30", "+380681111222", "2013-12-02 22:05:27"),
    ("Bondarenko", "Dmytro", "Petrovych", "1988-06-17", "+380671212121", "2017-05-30 11:40:15"),
    ("Kharchenko", "Iryna", "Andriivna", "1993-04-20", "+380961111999", "2019-03-08 07:50:00"),
    ("Lysenko", "Yurii", "Mykolaiovych", "1980-10-10", "+380971234321", "2010-10-14 16:25:33"),
    ("Boiko", "Yana", "Romanivna", "2002-08-08", "+380973334455", "2024-06-20 13:15:48"),
]



cursor.executemany("""
INSERT INTO users (last_name, first_name, sur_name, birth_date, phone_number, connection_date)
VALUES (?, ?, ?, ?, ?, ?)
""", users)


# Додаємо типи послуг
services = [
    (1, "mobile_connection"),
    (2, "mobile_internet"),
    (3, "home_internet"),
    (4, "television"),
]

cursor.executemany("INSERT INTO services (service_id, service_name) VALUES (?, ?)", services)

# Додаємо user_services (1-2 послуги на користувача)
user_services = [
    (1, 1, 100.0),
    (1, 2, 70.0),
    (2, 3, 120.0),
    (3, 4, 150.0),
    (4, 1, 90.0),
    (5, 2, 60.0),
    (6, 3, 110.0),
    (7, 1, 80.0),
    (8, 4, 130.0),
    (9, 1, 100.0),
    (9, 2, 60.0),
    (10, 3, 105.0),
]

cursor.executemany("""
INSERT INTO user_services (user_id, service_id, monthly_fee)
VALUES (?, ?, ?)
""", user_services)

# Додаємо відгуки (5 негативних, 3 позитивних, 1 нейтральний, 1 без відгуку)
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

reviews = [
    # негативні
    (1, "Зв'язок часто пропадає, неможливо додзвонитись", now),
    (2, "Домашній інтернет постійно лагає і часто відключається", now),
    (3, "Якість телебачення дуже погана, канали не працюють", now),
    (4, "Дуже дорого і нічого не працює", now),
    (5, "Служба підтримки ігнорує звернення", now),

    # позитивні
    (6, "Все працює чудово, дякую за якісний інтернет!", now),
    (7, "Швидкий мобільний інтернет, задоволений", now),
    (8, "Зручний сервіс, легко оплатити і підключити", now),

    # нейтральний
    (9, "Послуги нормальні, але іноді бувають проблеми", now),

    # 10-й користувач — без відгуку
]

cursor.executemany("""
INSERT INTO reviews (user_id, review_text, created_at)
VALUES (?, ?, ?)
""", reviews)

conn.commit()
conn.close()
print("Базу заповнено тестовими даними.")

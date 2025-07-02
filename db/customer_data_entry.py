from db.add_client_db import Client
from datetime import datetime

print("=== Введення нового клієнта ===")
last_name = input("Прізвище: ")
first_name = input("Ім'я: ")
sur_name = input("По батькові: ")
birth_date = input("Дата народження (YYYY-MM-DD): ")
phone_number = input("Номер телефону: ")

# Дата підключення — автоматично поточна
connection_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Вводимо підписки
print("Оберіть послуги (ID) для підключення. Доступні:")
services = {
    1: "mobile_connection",
    2: "mobile_internet",
    3: "home_internet",
    4: "television",
}
for sid, name in services.items():
    print(f"{sid}. {name}")

subscriptions = []
while True:
    sid = input("ID послуги (або натисніть Enter щоб завершити): ")
    if not sid:
        break
    try:
        sid = int(sid)
        if sid in services:
            fee = float(input("Місячна абонплата: "))
            subscriptions.append((sid, fee))
        else:
            print("Невірний ID послуги.")
    except ValueError:
        print("Невірне число.")

# Створення та додавання клієнта
client = Client(
    last_name=last_name,
    first_name=first_name,
    sur_name=sur_name,
    birth_date=birth_date,
    phone_number=phone_number,
    connection_date=connection_date,
    subscriptions=subscriptions
)

client.add_to_db()
print("Клієнта успішно додано.")

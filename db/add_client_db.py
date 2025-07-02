import sqlite3
class Client:
    def __init__(self, last_name, first_name, sur_name, birth_date, phone_number, connection_date, subscriptions=None):
        self.last_name = last_name
        self.first_name = first_name
        self.sur_name = sur_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.connection_date = connection_date
        self.subscriptions = subscriptions or []  # список кортежей: (service_id, monthly_fee)

    def add_to_db(self, db_path="kyivstar_feedback.db"):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (last_name, first_name, sur_name, birth_date, phone_number, connection_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.last_name, self.first_name, self.sur_name,
              self.birth_date, self.phone_number, self.connection_date))

        user_id = cursor.lastrowid  # получаем ID только что добавленного пользователя

        for service_id, fee in self.subscriptions:
            cursor.execute("""
                INSERT INTO user_services (user_id, service_id, monthly_fee)
                VALUES (?, ?, ?)
            """, (user_id, service_id, fee))

        conn.commit()
        conn.close()

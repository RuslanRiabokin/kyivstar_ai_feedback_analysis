import sqlite3
from datetime import datetime

class ReviewManager:
    def __init__(self, db_path="kyivstar_feedback.db"):
        # Підключення до бази даних
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_user_id_by_phone(self, phone_number):
        # Отримуємо user_id за номером телефону
        self.cursor.execute("""
            SELECT user_id FROM users WHERE phone_number = ?
        """, (phone_number,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def add_review(self, phone_number, review_text):
        # Пошук користувача
        user_id = self.get_user_id_by_phone(phone_number)
        if not user_id:
            print("❌ Користувача з таким номером не знайдено.")
            return

        # Поточна дата і час
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Додавання відгуку
        self.cursor.execute("""
            INSERT INTO reviews (user_id, review_text, created_at)
            VALUES (?, ?, ?)
        """, (user_id, review_text, created_at))
        self.conn.commit()
        print("✅ Відгук успішно додано.")

    def close(self):
        # Закриття з'єднання з базою
        self.conn.close()

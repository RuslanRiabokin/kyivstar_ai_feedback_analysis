import sqlite3

DB_PATH = "kyivstar_feedback.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

# Додає новий стовпець, якщо його ще немає
def add_column_if_not_exists(table_name, column_name, column_type):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")
    existing_columns = [col[1] for col in cursor.fetchall()]

    if column_name not in existing_columns:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        print(f"✅ Стовпець '{column_name}' додано в таблицю '{table_name}'.")
    else:
        print(f"ℹ️ Стовпець '{column_name}' вже існує в таблиці '{table_name}'.")

    conn.commit()
    conn.close()

# Створює таблицю, якщо її ще не існує
def create_table_if_not_exists(table_name, columns_sql: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns_sql}
        )
    """)
    print(f"✅ Таблицю '{table_name}' створено або вже існує.")

    conn.commit()
    conn.close()

# Додати таблицю з FOREIGN KEY-зв'язками
def create_related_table_if_not_exists(table_name, columns_sql: str, foreign_keys_sql: str = ""):
    conn = get_connection()
    cursor = conn.cursor()

    full_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns_sql}
            {',' if foreign_keys_sql else ''}
            {foreign_keys_sql}
        )
    """
    cursor.execute(full_sql)
    print(f"✅ Залежну таблицю '{table_name}' створено або вже існує.")

    conn.commit()
    conn.close()

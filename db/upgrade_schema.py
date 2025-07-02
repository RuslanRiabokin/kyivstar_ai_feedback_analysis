from db.schema_manager import add_column_if_not_exists

# Додаємо поле 'sur_name' до таблиці users
add_column_if_not_exists("users", "connection_date", "TEXT")

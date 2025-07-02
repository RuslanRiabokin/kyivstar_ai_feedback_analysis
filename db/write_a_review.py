from add_review import ReviewManager

manager = ReviewManager()

print("=== Залишити відгук ===")
phone = input("Введіть свій номер телефону (наприклад, +380962223344): ").strip()
text = input("Введіть текст відгуку: ").strip()

manager.add_review(phone, text)
manager.close()

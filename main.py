# Завдання 1: Створення телефонної книги
contacts = [
    {"ім'я": "Олег", "прізвище": "Коваль", "телефон": "123456789", "місто": "Київ"},
    {"ім'я": "Ірина", "прізвище": "Сидоренко", "телефон": "987654321", "місто": "Львів"},
    {"ім'я": "Марина", "прізвище": "Іванова", "телефон": "555666777", "місто": "Одеса"},
    {"ім'я": "Петро", "прізвище": "Дмитренко", "телефон": "222333444", "місто": "Київ"},
    {"ім'я": "Анна", "прізвище": "Мельник", "телефон": "999888777", "місто": "Харків"}
]

def print_contacts(contact_list):
    print(f"{'Ім\'я':<10} {'Прізвище':<15} {'Телефон':<12} {'Місто':<10}")
    print("-" * 50)
    for c in contact_list:
        print(f"{c['ім\'я']:<10} {c['прізвище']:<15} {c['телефон']:<12} {c['місто']:<10}")

print("Повний перелік контактів:")
print_contacts(contacts)

# Завдання 2: Розширений пошук
def search_contacts(field):
    query = input(f"Введіть {field}: ").strip()
    if not query:
        print("Порожній ввід.")
        return
    result = [c for c in contacts if c[field].lower() == query.lower()]
    if result:
        print_contacts(result)
    else:
        print("Контактів не знайдено.")

print("\n=== Пошук контактів ===")
search_contacts("ім'я")
search_contacts("прізвище")
search_contacts("місто")

# Завдання 3: Оновлення, видалення, аналітика
def update_contact():
    phone = input("Введіть телефон контакту для оновлення: ").strip()
    contact = next((c for c in contacts if c["телефон"] == phone), None)
    if not contact:
        print("Контакт не знайдено.")
        return
    confirm = input("Підтвердити оновлення (так/ні)? ").lower()
    if confirm == "так":
        contact["ім'я"] = input("Нове ім'я: ") or contact["ім'я"]
        contact["прізвище"] = input("Нове прізвище: ") or contact["прізвище"]
        contact["місто"] = input("Нове місто: ") or contact["місто"]
        print("Контакт оновлено.")
        print_contacts([contact])

def delete_contact():
    phone = input("Введіть телефон контакту для видалення: ").strip()
    contact = next((c for c in contacts if c["телефон"] == phone), None)
    if not contact:
        print("Контакт не знайдено.")
        return
    confirm = input("Підтвердити видалення (так/ні)? ").lower()
    if confirm == "так":
        contacts.remove(contact)
        print("Контакт видалено.")

def analytics():
    cities = {c['місто'] for c in contacts}
    print("\nУнікальні міста:", cities)
    city_count = {}
    for c in contacts:
        city_count[c['місто']] = city_count.get(c['місто'], 0) + 1
    print("Кількість контактів у містах:")
    for city, count in city_count.items():
        print(f"{city}: {count}")
    max_city = max(city_count, key=city_count.get)
    print(f"Місто з найбільшою кількістю контактів: {max_city}")

print("\n=== Оновлення/Видалення контактів ===")
update_contact()
delete_contact()
print("\nАктуальний список контактів:")
print_contacts(contacts)
analytics()

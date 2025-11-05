# відповідно до свого варіанту написати програму, яка створює об’єкт JSON 
# для збереження даних із заданої предметної області та виконує обробку даних.

#! Задано дані про кількість деталей п’яти видів, які випускав цех кожен день. 
#! Скласти програму, яка визначає загальну вартість деталей за один тиждень.

import json

FILE = "details.json"
RESULT_FILE = "details_result.json"

def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Помилка: файл не вдалося відкрити!")
        return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_data():
    data = load_data()
    print("\n=== Вміст JSON файлу ===")
    for d in data:
        print(d)

def add_record():
    data = load_data()
    name = input("Назва деталі: ")
    price = float(input("Ціна за одиницю: "))
    daily = []

    print("Введіть кількість виготовлених деталей за кожен день (7 днів):")
    for i in range(7):
        daily.append(int(input(f"День {i+1}: ")))

    data.append({"name": name, "price": price, "daily": daily})
    save_data(data)
    print("Запис додано!")

def delete_record():
    data = load_data()
    name = input("Введіть назву деталі для видалення: ")
    new_data = [item for item in data if item["name"] != name]

    if len(new_data) == len(data):
        print("Такої деталі не знайдено!")
    else:
        save_data(new_data)
        print("Запис видалено!")

def search():
    data = load_data()
    name = input("Введіть назву деталі для пошуку: ")
    results = [item for item in data if item["name"] == name]

    if results:
        print("Знайдено:", results[0])
    else:
        print("Нічого не знайдено")

def calc_total():
    data = load_data()
    results = []

    for item in data:
        total_amount = sum(item["daily"])        
        total_price = total_amount * item["price"]  
        results.append({"name": item["name"], "total_price": total_price})

    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("Результат збережено у:", RESULT_FILE)

while True:
    print("\n=== Меню ===")
    print("1 - Показати дані")
    print("2 - Додати запис")
    print("3 - Видалити запис")
    print("4 - Пошук за назвою")
    print("5 - Обчислити загальну вартість за тиждень")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1": show_data()
    elif choice == "2": add_record()
    elif choice == "3": delete_record()
    elif choice == "4": search()
    elif choice == "5": calc_total()
    elif choice == "0":
        print("Завершення роботи...")
        break
    else:
        print("Невірний вибір!")

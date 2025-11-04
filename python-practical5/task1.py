# Задано дані про потужність двигуна (в кінських силах – к.с.) 
# і вартість n=10 легкових автомобілів. Скласти програму, 
# яка визначає загальну вартість автомобілів, 
# у яких потужність двигуна перевищує 100 к.с.

# Словник автомобілів: ключ — назва/модель, значення — словник характеристик
cars = {
    "BMW X5": {"power": 300, "price": 55000},
    "Audi A4": {"power": 150, "price": 32000},
    "Toyota Corolla": {"power": 98, "price": 22000},
    "Honda Civic": {"power": 110, "price": 26000},
    "Ford Focus": {"power": 105, "price": 24000},
    "Mercedes C200": {"power": 184, "price": 40000},
    "Volkswagen Golf": {"power": 90, "price": 20000},
    "Kia Sportage": {"power": 135, "price": 28000},
    "Hyundai Tucson": {"power": 170, "price": 35000},
    "Skoda Octavia": {"power": 115, "price": 27000}
}

def print_all(cars_dict):
    print("\nСписок автомобілів:")
    for model, data in cars_dict.items():
        print(f"{model}: потужність = {data['power']} к.с., ціна = {data['price']} $")

def add_car(cars_dict):
    try:
        model = input("Введіть назву моделі: ")
        power = int(input("Введіть потужність (к.с.): "))
        price = int(input("Введіть ціну ($): "))
        cars_dict[model] = {"power": power, "price": price}
        print("Автомобіль додано.")
    except ValueError:
        print("Помилка: потужність і ціна повинні бути числами.")

def delete_car(cars_dict):
    model = input("Введіть назву моделі для видалення: ")
    if model in cars_dict:
        del cars_dict[model]
        print("Автомобіль видалено.")
    else:
        print("Такої моделі немає у словнику.")

def print_sorted(cars_dict):
    print("\nСловник у відсортованому порядку:")
    for model in sorted(cars_dict.keys()):
        data = cars_dict[model]
        print(f"{model}: потужність = {data['power']} к.с., ціна = {data['price']} $")

def total_cost_power_over_100(cars_dict):
    total = sum(data["price"] for data in cars_dict.values() if data["power"] > 100)
    print(f"\nЗагальна вартість авто з потужністю > 100 к.с.: {total} $")

while True:
    print("\n--- Меню ---")
    print("1. Показати всі автомобілі")
    print("2. Додати автомобіль")
    print("3. Видалити автомобіль")
    print("4. Перегляд відсортованого словника")
    print("5. Обчислити сумарну вартість авто > 100 к.с.")
    print("0. Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print_all(cars)
    elif choice == "2":
        add_car(cars)
    elif choice == "3":
        delete_car(cars)
    elif choice == "4":
        print_sorted(cars)
    elif choice == "5":
        total_cost_power_over_100(cars)
    elif choice == "0":
        print("Завершення роботи...")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

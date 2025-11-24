# Завдання 1
# Перетворіть словник, створений у практичній роботі №5, на датафрейм. 
# За потреби доповніть словник новими даними (наприклад, додайте ще кілька записів або 
# стовпців із додатковими характеристиками об’єктів), виведіть вміст словника на екран.
# Виконайте базовий аналіз даних:
    # Виведіть перші 3 рядки DataFrame (df.head(3)).
    # Перевірте типи даних (df.dtypes).
    # Визначте кількість рядків і стовпців (df.shape).
    # Отримайте описову статистику (df.describe())
# Додайте новий стовпець , який буде містити розрахункові значення. Наприклад, обчисліть загальну вартість продажу товару для кожного запису. Виконайте фільтрацію даних, наприклад, виберіть товари з ціною понад 10 000 грн. Виконайте сортування даних, наприклад, за спаданням ціни або кількості.
# Виконайте групування даних та знайдіть середнє значення.
# Виконайте додаткові операції агрегації, наприклад:
    # знайдіть максимальну суму продажів у категорії;
    # визначте кількість унікальних товарів.

import pandas as pd

# Дані з практичної роботи №5
cars = {
    "BMW X5": {"power": 300, "price": 55000, "year": 2020},
    "Audi A4": {"power": 150, "price": 32000, "year": 2018},
    "Toyota Corolla": {"power": 98, "price": 22000, "year": 2019},
    "Honda Civic": {"power": 110, "price": 26000, "year": 2020},
    "Ford Focus": {"power": 105, "price": 24000, "year": 2017},
    "Mercedes C200": {"power": 184, "price": 40000, "year": 2021},
    "Volkswagen Golf": {"power": 90, "price": 20000, "year": 2016},
    "Kia Sportage": {"power": 135, "price": 28000, "year": 2022},
    "Hyundai Tucson": {"power": 170, "price": 35000, "year": 2021},
    "Skoda Octavia": {"power": 115, "price": 27000, "year": 2019}
}

df = pd.DataFrame.from_dict(cars, orient='index')
df.index.name = "model"

print("=== DataFrame ===")
print(df)

print("\n=== Перші 3 рядки ===")
print(df.head(3))

print("\n=== Типи даних ===")
print(df.dtypes)

print("\n=== Кількість рядків і стовпців ===")
print(df.shape)

print("\n=== Описова статистика ===")
print(df.describe())

df["sale_value"] = df["price"] * 1.2

print("\n=== DataFrame з новим стовпцем sale_value ===")
print(df)


filtered = df[df["price"] > 30000]

print("\n=== Авто з ціною > 30000$ ===")
print(filtered)

sorted_by_price = df.sort_values(by="price", ascending=False)

print("\n=== Сортування за спаданням ціни ===")
print(sorted_by_price)


def classify_power(p):
    if p <= 120:
        return "Слабкі"
    elif p <= 180:
        return "Середні"
    else:
        return "Потужні"

df["power_class"] = df["power"].apply(classify_power)

grouped = df.groupby("power_class")["price"].mean()

print("\n=== Середня ціна за класами потужності ===")
print(grouped)

max_sale = df.groupby("year")["sale_value"].max()
unique_models = df.index.nunique()

print("\n=== Максимальна сума продажів за роками ===")
print(max_sale)

print("\n=== Кількість унікальних моделей ===")
print(unique_models)

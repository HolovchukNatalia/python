# Завдання 3

# Побудуйте кругову діаграму на основі даних з предметної області лабораторної роботи №12(5). 
# Використайте бібліотеку Matplotlib. На круговій діаграмі мають відображатися значення 
# показників у відсотках, наприклад, відсоток дівчат та хлопців, які навчаються у певному класі, 
# сектори діаграми повинні бути розфарбовані в різний колір, на діаграмі мають бути підписи.

import matplotlib.pyplot as plt
import numpy as np

# Дані з 5 практичної(потрібно потужність автомобілів)
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
more_100 = sum(data["power"] > 100 for data in cars.values())
less_or_equal_100 = sum(data["power"] <= 100 for data in cars.values())

labels = ["Понад 100 к.с.", "100 к.с. і менше"]
data = [more_100, less_or_equal_100]

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} авто)"

wedges, texts, autotexts = ax.pie(
    data,
    autopct=lambda pct: func(pct, data),
    textprops=dict(color="white")
)

ax.legend(
    wedges,
    labels,
    title="Категорії потужності",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Розподіл автомобілів за потужністю двигуна")

plt.show()
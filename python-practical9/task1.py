# Напишіть програму для обробки .csv файла та збереження результатів у інший .csv файл. 
# У програмі реалізувати обробку помилок відкриття файлу за допомогою конструкції try-except.

#! Знайти дані Inflation, consumer prices (annual %) для України за 1991-2019 роки.
#! Вивести вміст .csv файлу на екран. Організувати пошук найнижчого та найвищого 
#! значень показника та записати результат пошуку у новий .csv файл.

import csv

INPUT_FILE = "API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_130173.csv"
OUTPUT_FILE = "inflation_ukraine_result.csv"
MIN_MAX_FILE = "inflation_min_max.csv"
COUNTRY_CODE = "UKR"

START_YEAR = 1991
END_YEAR = 2019

years = list(range(START_YEAR, END_YEAR + 1))
inflation_data = {}

try:
    with open(INPUT_FILE, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
except FileNotFoundError:
    print(f"Помилка: файл '{INPUT_FILE}' не знайдено.")
    exit()
except Exception as e:
    print(f"Помилка відкриття файлу: {e}")
    exit()

for row in rows:
    if len(row) > 1 and row[1] == COUNTRY_CODE:
        for i, year in enumerate(rows[4]):
            if year.isdigit() and START_YEAR <= int(year) <= END_YEAR:
                value = row[i]
                inflation_data[int(year)] = value if value.strip() != "" else "даних немає"
        break

try:
    with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Inflation"])
        for year in years:
            writer.writerow([year, inflation_data.get(year, "даних немає")])
except Exception as e:
    print(f"Помилка запису у файл: {e}")
    exit()

print("Інфляція в Україні (1991–2019):")
for year in years:
    print(f"{year}: {inflation_data.get(year, 'даних немає')}")

numeric_values = {y: float(v) for y, v in inflation_data.items() if v not in ("", "даних немає")}

if numeric_values:
    min_year = min(numeric_values, key=numeric_values.get)
    max_year = max(numeric_values, key=numeric_values.get)

    print(f"\nНайнижча інфляція: {min_year} → {numeric_values[min_year]}%")
    print(f"Найвища інфляція: {max_year} → {numeric_values[max_year]}%")

    try:
        with open(MIN_MAX_FILE, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Year", "Inflation"])
            writer.writerow(["Найнижча інфляція", min_year, numeric_values[min_year]])
            writer.writerow(["Найвища інфляція", max_year, numeric_values[max_year]])
        print(f"\nФайл з мін/макс інфляцією збережено: {MIN_MAX_FILE}")
    except Exception as e:
        print(f"Помилка запису у файл {MIN_MAX_FILE}: {e}")

else:
    print("\nНемає числових даних для визначення максимуму/мінімуму.")

print(f"\nРезультат збережено у файлі: {OUTPUT_FILE}")

# Завдання 2
# Візуалізація даних з порталу відкритих даних https://databank.worldbank.org/home.aspx. 
# Використайте бібліотеку Matplotlib.
# Самостійно оберіть предметну область, наприклад, Education Statistics, 
# з якої візьміть показник, наприклад, Children out of school, primary в динаміці 
# за останніх двадцять років (або інший період, якщо дані для цього періоду на порталі відсутні) 
# для України та однієї з країн світу на вибір, наприклад, США.  
# Сформуйте масив даних для побудови графіку та напишіть програму для їх візуалізації.
# 2.1. На одній координатній осі побудуйте графіки, що показують динаміку 
# показника для двох країн, підпишіть осі –  по осі Х має відображатися рік, 
# а по осі Y має відображатися значення показника.
# 2.2 Побудуйте стовпчасті діаграми, які відображатимуть значення показника 
# для кожної з країн. Назву країни для побудови діаграми має вводити 
# користувач з клавіатури.


import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

indicator = "SE.PRM.UNER"  
countries = ["UA", "PL"]    
years = "2005:2025"

# Формуємо URL World Bank API та отримуємо дані
url = f"http://api.worldbank.org/v2/country/{';'.join(countries)}/indicator/{indicator}?date={years}&format=json"

response = requests.get(url)
data_json = response.json()

if not data_json or len(data_json) < 2:
    print("Error fetching data from World Bank API")
    exit()

data_list = data_json[1]  
records = []
for entry in data_list:
    records.append({
        "Country": entry["country"]["value"],
        "Year": int(entry["date"]),
        "Value": entry["value"]
    })

df = pd.DataFrame(records)

df_ua = df[df["Country"] == "Ukraine"].sort_values("Year").set_index("Year")
df_ua = df_ua.reindex(range(2005, 2026)) 
df_ua["Country"] = "Ukraine"
df_ua["Value"] = df_ua["Value"].interpolate(method='linear')  

df_pl = df[df["Country"] == "Poland"].sort_values("Year").set_index("Year")
df_pl = df_pl.reindex(range(2005, 2026))
df_pl["Country"] = "Poland"
df_pl["Value"] = df_pl["Value"].interpolate(method='linear')

x_ua_smooth = np.linspace(df_ua.index.min(), df_ua.index.max(), 300)
x_pl_smooth = np.linspace(df_pl.index.min(), df_pl.index.max(), 300)

spl_ua = make_interp_spline(df_ua.index, df_ua["Value"], k=3)
spl_pl = make_interp_spline(df_pl.index, df_pl["Value"], k=3)

y_ua_smooth = spl_ua(x_ua_smooth)
y_pl_smooth = spl_pl(x_pl_smooth)

plt.figure(figsize=(10, 6))
plt.plot(x_ua_smooth, y_ua_smooth, label="Ukraine", color='blue', linewidth=2)
plt.plot(x_pl_smooth, y_pl_smooth, label="Poland", color='red', linewidth=2)
plt.title("Children out of school (primary) – Ukraine vs Poland (2005-2025)")
plt.xlabel("Year")
plt.ylabel("Number of children out of school")
plt.legend()
plt.grid(True)
plt.show()

# Стовпчасті діаграми
country_input = input("Enter country name (Ukraine or Poland): ").strip()

if country_input not in df["Country"].unique():
    print("Country not found!")
else:
    df_country = df[df["Country"] == country_input].sort_values("Year").set_index("Year")
    df_country = df_country.reindex(range(2005, 2026))
    df_country["Value"] = df_country["Value"].interpolate(method='linear')
    
    plt.figure(figsize=(10, 6))
    plt.bar(df_country.index, df_country["Value"], color='green')
    plt.title(f"Children out of school (primary) – {country_input} (2005-2025)")
    plt.xlabel("Year")
    plt.ylabel("Number of children out of school")
    plt.xticks(rotation=45)
    plt.show()

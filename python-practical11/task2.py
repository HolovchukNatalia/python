import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comptagevelo2009.csv')

print("=== Перші рядки ===")
print(df.head())

print("\n=== Інформація про DataFrame ===")
print(df.info())

print("\n=== Описова статистика ===")
print(df.describe())


if 'Unnamed: 1' in df.columns:
    df = df.drop(columns=['Unnamed: 1'])

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


tracks = ['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf']
total_annual = df[tracks].sum().sum()
print("\n=== Загальна кількість велосипедистів за рік ===")
print(total_annual)


total_per_track = df[tracks].sum()
print("\n=== Загальна кількість велосипедистів по доріжках ===")
print(total_per_track)

df['Month'] = df['Date'].dt.month
popular_month = df.groupby('Month')[tracks[:3]].sum().idxmax()
print("\n=== Найпопулярніший місяць для кожної з трьох доріжок ===")
print(popular_month)


monthly_counts = df.groupby('Month')['Berri1'].sum()

plt.figure(figsize=(10,6))
plt.plot(monthly_counts.index, monthly_counts.values, marker='o', linestyle='-')
plt.title("Завантаженість доріжки Berri1 по місяцях, 2009")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(1,13))
plt.grid(True)
plt.show()

df = df.set_index('Date')

track_columns = [col for col in df.columns if col != 'Month']

plt.figure(figsize=(15,10))
df[track_columns].plot(figsize=(15, 10))
plt.title("Графік використання велодоріжок за 2009 рік")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.show()

# """
# Приклад 1: NumPy - Обчислення статистичних показників для набору даних продажів
# """

# import numpy as np

# # Дані про продажі за тиждень
# sales = np.array([120, 135, 148, 132, 165, 178, 155])

# # Статистичні показники
# mean_sales = np.mean(sales)
# median_sales = np.median(sales)
# std_sales = np.std(sales)
# max_sales = np.max(sales)
# min_sales = np.min(sales)

# print("=" * 50)
# print("АНАЛІЗ ПРОДАЖІВ ЗА ТИЖДЕНЬ")
# print("=" * 50)
# print(f'Дані продажів: {sales}')
# print(f'\nСередні продажі: {mean_sales:.2f}')
# print(f'Медіана: {median_sales:.2f}')
# print(f'Стандартне відхилення: {std_sales:.2f}')
# print(f'Максимум: {max_sales}')
# print(f'Мінімум: {min_sales}')
# print("=" * 50)

# """
# Приклад 2: Pandas - Аналіз даних про клієнтів інтернет-магазину
# """

# import pandas as pd

# # Створення DataFrame з даними про клієнтів
# data = {
#     'Ім\'я': ['Олена', 'Петро', 'Марія', 'Іван', 'Ольга'],
#     'Вік': [25, 34, 29, 42, 31],
#     'Місто': ['Київ', 'Львів', 'Київ', 'Одеса', 'Львів'],
#     'Сума_покупок': [1200, 850, 2100, 670, 1450]
# }

# df = pd.DataFrame(data)

# print("=" * 60)
# print("АНАЛІЗ ДАНИХ КЛІЄНТІВ ІНТЕРНЕТ-МАГАЗИНУ")
# print("=" * 60)

# print("\nВсі дані про клієнтів:")
# print(df)

# # Аналіз даних
# print(f'\n\nСередній вік клієнтів: {df["Вік"].mean():.1f} років')

# print('\nСередня сума покупок за містом:')
# print(df.groupby('Місто')['Сума_покупок'].mean())

# # Фільтрація клієнтів з покупками > 1000
# active_clients = df[df['Сума_покупок'] > 1000]
# print(f'\n\nАктивні клієнти (покупки > 1000 грн): {len(active_clients)}')
# print(active_clients[['Ім\'я', 'Сума_покупок']])

# print("\n" + "=" * 60)

# """
# Приклад 3: Matplotlib - Візуалізація тенденцій продажів протягом року
# """

# import matplotlib.pyplot as plt
# import numpy as np
# import os

# # Налаштування для коректного відображення українських символів
# plt.rcParams['font.family'] = 'DejaVu Sans'

# # Дані про продажі по місяцях
# months = ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 
#           'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру']
# sales = [45, 52, 61, 58, 70, 85, 92, 88, 79, 73, 68, 95]

# # Створення графіка
# plt.figure(figsize=(12, 6))
# plt.plot(months, sales, marker='o', linewidth=2, 
#          color='#2E86AB', markersize=8, label='Продажі')

# # Додавання середньої лінії
# avg_sales = np.mean(sales)
# plt.axhline(y=avg_sales, color='red', linestyle='--', 
#             linewidth=1.5, label=f'Середнє: {avg_sales:.1f}')

# plt.title('Динаміка продажів протягом року', fontsize=16, fontweight='bold')
# plt.xlabel('Місяць', fontsize=12)
# plt.ylabel('Продажі (тис. грн)', fontsize=12)
# plt.grid(True, alpha=0.3)
# plt.legend()
# plt.tight_layout()

# # Збереження графіка в поточну директорію
# output_file = 'sales_trend.png'
# plt.savefig(output_file, dpi=300, bbox_inches='tight')
# print("=" * 60)
# print(f"Графік успішно створено та збережено як '{output_file}'")
# print(f"Повний шлях: {os.path.abspath(output_file)}")
# print("=" * 60)

# # Відображення графіка
# plt.show()

# """
# Приклад 4: Scikit-learn - Прогнозування ціни нерухомості на основі характеристик
# """

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import numpy as np

# # Дані: площа (м²), кількість кімнат, поверх
# X = np.array([
#     [50, 2, 3], 
#     [75, 3, 5], 
#     [100, 4, 2], 
#     [120, 4, 7], 
#     [65, 2, 1], 
#     [90, 3, 4]
# ])

# # Ціна (тис. $)
# y = np.array([45, 68, 95, 115, 58, 82])

# print("=" * 70)
# print("ПРОГНОЗУВАННЯ ЦІНИ НЕРУХОМОСТІ")
# print("=" * 70)

# print("\nВхідні дані (площа м², кімнати, поверх):")
# print(X)
# print("\nЦіни (тис. $):")
# print(y)

# # Розділення на тренувальну та тестову вибірки
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=42
# )

# print(f"\nРозмір тренувальної вибірки: {len(X_train)}")
# print(f"Розмір тестової вибірки: {len(X_test)}")

# # Навчання моделі
# model = LinearRegression()
# model.fit(X_train, y_train)

# print("\nКоефіцієнти моделі:")
# print(f"  - Вплив площі: {model.coef_[0]:.4f}")
# print(f"  - Вплив кількості кімнат: {model.coef_[1]:.4f}")
# print(f"  - Вплив поверху: {model.coef_[2]:.4f}")
# print(f"  - Зміщення: {model.intercept_:.4f}")

# # Прогнозування
# y_pred = model.predict(X_test)

# print("\n" + "-" * 70)
# print("РЕЗУЛЬТАТИ ПРОГНОЗУВАННЯ:")
# print("-" * 70)
# for i, (test_data, real_price, pred_price) in enumerate(zip(X_test, y_test, y_pred), 1):
#     print(f"Квартира {i}: {test_data[0]:.0f}м², {test_data[1]:.0f} кімнат, {test_data[2]:.0f} поверх")
#     print(f"  Реальна ціна: ${real_price:.1f}k | Прогноз: ${pred_price:.1f}k | Різниця: ${abs(real_price - pred_price):.1f}k")

# print("\n" + "=" * 70)
# print("МЕТРИКИ ЯКОСТІ МОДЕЛІ:")
# print("=" * 70)
# print(f'R² score (коефіцієнт детермінації): {r2_score(y_test, y_pred):.3f}')
# print(f'RMSE (середньоквадратична помилка): ${np.sqrt(mean_squared_error(y_test, y_pred)):.2f}k')
# print("=" * 70)

# # Приклад прогнозування для нової квартири
# print("\nПРИКЛАД: Прогноз для квартири 85м², 3 кімнати, 6 поверх:")
# new_apartment = np.array([[85, 3, 6]])
# predicted_price = model.predict(new_apartment)
# print(f"Прогнозована ціна: ${predicted_price[0]:.2f}k")

"""
Приклад 5: SciPy - Статистичний аналіз A/B тестування
"""

from scipy import stats
import numpy as np

# Дані конверсії для двох варіантів сайту
# Варіант A: контрольна група (1 = конверсія, 0 = відмова)
conversions_a = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 
                          0, 1, 0, 1, 1, 0, 0, 1, 1, 0])

# Варіант B: експериментальна група
conversions_b = np.array([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 
                          1, 1, 0, 1, 1, 1, 0, 1, 1, 1])

print("=" * 70)
print("A/B ТЕСТУВАННЯ САЙТУ - СТАТИСТИЧНИЙ АНАЛІЗ")
print("=" * 70)

print(f"\nРозмір вибірки A: {len(conversions_a)} користувачів")
print(f"Розмір вибірки B: {len(conversions_b)} користувачів")

# Базові статистики
conv_rate_a = conversions_a.mean()
conv_rate_b = conversions_b.mean()
conversions_count_a = conversions_a.sum()
conversions_count_b = conversions_b.sum()

print("\n" + "-" * 70)
print("РЕЗУЛЬТАТИ:")
print("-" * 70)
print(f"Варіант A (контроль):")
print(f"  - Конверсій: {conversions_count_a} з {len(conversions_a)}")
print(f"  - Коефіцієнт конверсії: {conv_rate_a:.1%}")

print(f"\nВаріант B (експеримент):")
print(f"  - Конверсій: {conversions_count_b} з {len(conversions_b)}")
print(f"  - Коефіцієнт конверсії: {conv_rate_b:.1%}")

print(f"\nАбсолютна різниця: {(conv_rate_b - conv_rate_a):.1%}")
print(f"Відносне покращення: {((conv_rate_b - conv_rate_a) / conv_rate_a * 100):.1f}%")

# T-тест для незалежних вибірок
t_statistic, p_value = stats.ttest_ind(conversions_a, conversions_b)

print("\n" + "=" * 70)
print("СТАТИСТИЧНА ЗНАЧУЩІСТЬ:")
print("=" * 70)
print(f'T-статистика: {t_statistic:.4f}')
print(f'P-value: {p_value:.4f}')

# Інтерпретація результатів
alpha = 0.05  # рівень значущості
print(f'\nРівень значущості (α): {alpha}')

if p_value < alpha:
    print(f'\n✓ ВИСНОВОК: Різниця є статистично значущою (p < {alpha})')
    print('  Варіант B показує значуще кращі результати.')
    print('  Рекомендація: впровадити варіант B.')
else:
    print(f'\n✗ ВИСНОВОК: Різниця не є статистично значущою (p >= {alpha})')
    print('  Спостережувана різниця може бути випадковою.')
    print('  Рекомендація: продовжити тестування або залишити варіант A.')

print("=" * 70)

# Додатковий тест: Chi-square для категоріальних даних
print("\nДОДАТКОВО: Chi-square тест")
print("-" * 70)
# Створення таблиці спряженості
contingency_table = np.array([
    [conversions_count_a, len(conversions_a) - conversions_count_a],
    [conversions_count_b, len(conversions_b) - conversions_count_b]
])
chi2, p_chi2, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Chi-square статистика: {chi2:.4f}")
print(f"P-value: {p_chi2:.4f}")
if p_chi2 < alpha:
    print("✓ Chi-square тест також підтверджує значущу різницю")
else:
    print("✗ Chi-square тест не показує значущої різниці")
# Завдання 1
# Побудуйте графік функції. Оберіть суцільний тип лінії, задайте колір та товщину графіку
#  та позначте осі, виведіть назву графіка на екран, вставте легенду. 
# Використайте бібліотеку Matplotlib.

# Y(x)=5*sin(10*x)*sin(3*x)/(x^(1/2)), x=[1...7]

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 7, 500)
y = 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.plot(x, y, color='blue', linestyle='-', linewidth=2, label='Y(x) = 5*sin(10x)*sin(3x)/√x')

plt.title("Графік функції Y(x)")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.legend()
plt.grid(True)
plt.show()

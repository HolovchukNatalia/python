# Реалізувати дві функції користувача в одній програмі.

import math
from task2 import product_of_even_or_odd 

def calculate_z(x):
	if x < 0:
		return "x не може бути від’ємним"
	if x >= 1:
		return "Для обчислення виразу x має бути меншим за 1"
	
	z = math.exp(math.sqrt(x)) / math.sqrt(1 - x)
	return z



x = float(input("Введіть значення x (0 ≤ x < 1): "))
print("Результат Z =", calculate_z(x))

N = int(input("Введіть ціле невід'ємне число N: "))
print("Добуток =", product_of_even_or_odd(N))
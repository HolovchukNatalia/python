# Реалізувати функцію, яка виконує операції над списками – 
# задану за варіантом та друк списку на екран. 
# Список користувач має вводити з клавіатури. 
# 
# Розбиття списку на два списки за вказаним порядковим номером 
# елемента для розбиття.

def split_list(my_list, index):
    first_part = my_list[:index]
    second_part = my_list[index:]
    return first_part, second_part

user_input = input("Введіть елементи списку через пробіл: ")
my_list = user_input.split()   

index = int(input("Введіть номер елемента для розбиття (починаючи з 1): "))
index -= 1

part1, part2 = split_list(my_list, index)

print("Перший список:", part1)
print("Другий список:", part2)

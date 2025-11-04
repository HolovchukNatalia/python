# Сортування бульбашкою.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for x in range(n - 1 - i):
            if lst[x] > lst[x + 1]:
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst

user_input = input("Введіть елементи списку через пробіл: ")

numbers = [int(x) for x in user_input.split()]

sorted_list = bubble_sort(numbers)

print("Відсортований список:", sorted_list)

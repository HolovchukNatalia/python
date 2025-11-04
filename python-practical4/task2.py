# Заповнити двовимірний масив розміром 7x7 таким чином, 
# як показано на рисунку. 
# Вивести масив на екран. Для виконання завдання використовуйте цикли.

array = []

for i in range(7):
    row = []
    for j in range(7):
        row.append(7 - j)
    array.append(row)

for row in array:
    for value in row:
        print(value, end=" ")
    print()

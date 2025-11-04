# Вводиться ціле число N (1<N<9), а виводяться рядки з числами або іншими символами (*, #), 
# які утворюють визначений «рисунок» (останній задається варіантом).

N = int(input("Введіть ціле число N (1 < N < 9): "))

if N <= 1 or N >= 9:
    print(" N має бути в межах (1 < N < 9)")
    exit()

mode = input("Введіть 'n' для чисел або символ (* або #): ")

indent = "  " * (N - 1)   

for i in range(N, 0, -1):
    print(indent, end="")
    for j in range(i, N + 1):
        if mode == 'n':
            print(j, end=" ")
        else:
            print(mode, end=" ")
    print()

for i in range(1, N + 1):
    print("  " * (N - i), end="")
    for j in range(i, 0, -1):
        if mode == 'n':
            print(j, end=" ")
        else:
            print(mode, end=" ")
    print()

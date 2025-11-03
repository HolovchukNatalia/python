# Задано речення. Скласти програму, яка визначає і виводить на екран 
# будь-яке його слово, що розпочинається на літеру «к».

sentence = input("Введіть речення: ")
words = sentence.split()  

for word in words:
    if word.lower().startswith("к"): 
        print(word)

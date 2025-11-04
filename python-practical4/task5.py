# Маємо множину символів {c, d}. Скласти програму, 
# яка додає до цієї множини множину голосних латинських 
# літер {а, е, i, о, u, y}.

def add_vowels_to_set(char_set):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    char_list = list(char_set)
    char_list.extend(list(vowels))
    return set(char_list)


initial_set = {'c', 'd'}

result = add_vowels_to_set(initial_set)

print("Результат множини:", result)

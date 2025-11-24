# Імпортувати бібліотеку NLTK та тексти із електронного архіву  текстів Project Gutenberg, 
# для виконання завдань взяти текст, заданий варіантом.
# Визначити кількість слів у тексті.
# Визначити 10 найбільш вживаних слів у тексті, побудувати на основі цих даних стовпчасту діаграму.
# Виконати видалення з тексту стоп-слів та пунктуації, після чого знову знайти 10 найбільш вживаних
# слів у тексті та побудувати на їх основі стовпчасту діаграму.

# carroll-alice.txt

import nltk
from nltk.corpus import stopwords, gutenberg
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('gutenberg')

text = gutenberg.raw('carroll-alice.txt')

tokenizer = RegexpTokenizer(r'\w+')  
words = tokenizer.tokenize(text.lower()) 

print(f"=== Кількість слів у тексті === {len(words)}")

counter = Counter(words)
most_common_words = counter.most_common(10)
print("\n=== 10 найбільш вживаних слів (всі слова) ===")
print(most_common_words)

words_list, counts = zip(*most_common_words)
plt.figure(figsize=(10,6))
plt.bar(words_list, counts, color='skyblue')
plt.title("10 найбільш вживаних слів (всі слова)")
plt.ylabel("Кількість")
plt.show()

stop_words = set(stopwords.words('english'))
words_filtered = [w for w in words if w not in stop_words]

counter_filtered = Counter(words_filtered)
most_common_filtered = counter_filtered.most_common(10)
print("\n=== 10 найбільш вживаних слів після очищення ===")
print(most_common_filtered)

words_list_f, counts_f = zip(*most_common_filtered)
plt.figure(figsize=(10,6))
plt.bar(words_list_f, counts_f, color='orange')
plt.title("10 найбільш вживаних слів (без стоп-слів та пунктуації)")
plt.ylabel("Кількість")
plt.show()

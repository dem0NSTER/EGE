"""
Все 5-буквенные слова, составленные из букв С, А, Н, Я. Вот начало списка:

ССССС
ССССА
ССССН
ССССЯ
...

Запишите слово, которое стоит на 10100002*112 - 111002-м месте от начала списка.
"""

from itertools import product
words = []

for i in product('саня', repeat=5): 
    word = ''.join(i)
    words.append(word)

index = int('1010000', 2) * int('11', 2) - int('11100', 2)
print(words[index])
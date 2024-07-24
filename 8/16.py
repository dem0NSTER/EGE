"""
Все 4-буквенные слова, в составе которых могут быть только буквы А, И, О, У, Э,
записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1.  АААА
2.  АААИ
3.  АААО
4.  АААУ
5.  АААЭ
……
Под каким номером стоит слово ИЭУЭ?
"""

import itertools 

list = []

for i in itertools.product('АИОУЭ', repeat=4): 
    word = ''.join(i)
    list.append(word)

words = sorted(list)
print(words.index("ИЭУЭ"))
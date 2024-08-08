"""
Все 4-буквенные слова, составленные из букв А, Ж, И, У записаны в алфавитном порядке.
Вот начало списка:
1. АААА
2. АААЖ
3. АААИ
4. АААУ
5. ААЖА
6. ААЖЖ
......
Определите какое слово стоит в списке раньше ЖИЖА или ЖУЖА и укажите его номер.
"""
import itertools

words = []

for i in itertools.product('АЖИУ', repeat=4): 
    word = ''.join(i)
    words.append(word)

words.sort()

index_1 = words.index('ЖИЖА')
index_2 = words.index('ЖУЖА')

if index_1 > index_2: 
    print(index_2 + 1)
else: 
    print(index_1 + 1)
"""
Все 4-буквенные слова, составленные из букв А, Б, Г, Д записаны в алфавитном порядке.
Вот начало списка:
1. АААА
2. АААБ
3. АААГ
4. АААД
5. ААБА
6. ААББ
......
Запишите позицию первого слова, которое состоит только из согласных и при 
этом буквы Б не стоят рядом
"""
import itertools 
words = []

for i in itertools.product("АБГД", repeat=4): 
    word = ''.join(i)
    words.append(word)

words.sort()

for word in words: 
    iv = False
    if word.count('А') != 0: 
        continue

    for i in range(len(word) - 1): 
        if word[i] == 'Б' and word[i + 1] == 'Б':
            iv = True
            break
    if iv: 
        continue
    print(word)
    print(words.index(word) + 1)
    break


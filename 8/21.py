"""
Вам дан набор, состоящий из букв слова «СБОРНИК». Из данного 
набора составляют 
последовательности длиной 7 символов, самое главное – 
символы могут повторяться. 
Ваша задача — определить количество кодов, в которых 
ровно одна буква О, слово 
не может начинаться на букву С и заканчиваться буквой Н. 
В ответ запишите целое число — 
количество таких слов
"""

import itertools 
c = 0

for i in itertools.product('СБОРНИК', repeat=7): 
    word = ''.join(i)

    if word.count('О') == 1 and word[0] != 'С' and word[-1] != 'Н': 
        c += 1

print(c)
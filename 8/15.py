"""
Вася составляет 6-буквенные слова, в которых могут быть использованы только буквы 
В, И, Ш, Н, Я, причём буква В используется не более одного раза. Каждая из других 
допустимых букв может встречаться в слове любое количество раз или не встречаться 
совсем. Слово не должно начинаться с буквы Ш и оканчиваться гласными буквами. 
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
"""

import itertools

c = 0

for i in itertools.product('ВИШНЯ', repeat=6):
    word = ''.join(i)
    if word.count('В') > 1: 
        continue
    if word[0] == 'Ш': 
        continue
    if word[-1] in 'ИЯ': 
        continue
    c += 1

print(c)

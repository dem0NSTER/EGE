"""
Нам дан набор, состоящий из букв С, Б, О, Р, Н, И, К. Из данного набора составляют слова 
длиной шесть символов, самое главное – символы могут повторяться. Все слова, которые 
возможно составить, расположили в алфавитном порядке, а наша задача – узнать 
под каким номером находится последнее слово, которое не начинается с буквы Р, 
содержит только две буквы Б и не более одной буквы К.
Пример списка слов:
1. ББББББ
2. БББББИ
3. БББББК
4. БББББН
5. БББББО
6. БББББР
7. БББББС
"""

import itertools 

res = []

for i in itertools.product('бикнорс', repeat=6):
    word = ''.join(i)

    res.append(word)

res.sort(reverse=True)
for word in res: 
    if word[0] != 'р' and word.count('б') == 2 and word.count('к') <= 1: 
        print(word)
        result = word
        break

res.sort()
print(res.index(result) + 1)

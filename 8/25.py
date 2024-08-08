"""
Некий Павел хочет узнать сколько слов можно получить, 
переставляя буквы в слове "телеграм". В ответ укажите 
олько число - количество перестановок.
"""

from itertools import permutations

words = []

for i in permutations('телеграм', r=len('телеграм')): 
    word = ''.join(i)
    words.append(word)

nw = set(words)
print(len(nw))

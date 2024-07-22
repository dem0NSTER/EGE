"""
Сколько существует различных двоичных кодов длиной 5 символов, содержащих 3 единицы? 
Двоичный код обязательно начинается с единицы.
"""
import itertools

c = 0

for i in itertools.product('01', repeat=5):
    word = ''.join(i)
    if word[0] != '1': 
        continue
    if word.count('1') != 3: 
        continue
    c += 1

print(c)

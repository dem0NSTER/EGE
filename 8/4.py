"""
Определите количество пятизначных чисел, записанных в девятеричной системе счисления, 
в записи которых цифра 3   встречается не более одного раза, 
на первом месте не может стоять нечетная цифра, 
а на последнем не могут стоять цифры 1 и 8  .
"""
from itertools import product

s = '012345678'
c = 0

for i in product(s, repeat=5): 
    word = ''.join(i)
    if word[0] == '0': 
        continue

    if word.count('3') > 1: 
        continue

    if int(word[0]) % 2 != 0: 
        continue

    if word[-1] == '1' or word[-1] == '8': 
        continue

    c += 1

print(c)

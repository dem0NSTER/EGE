"""
Сколько существует шестнадцатеричных трёхзначных чисел, в которых все цифры 
различны и никакие две чётные или две нечётные цифры не стоят рядом?
"""

import itertools 

res = 0

for i in itertools.permutations('1234567890abcdef', r=3): 
    
    j = False

    word = ''.join(i)
    print(word)

    if word[0] == '0': 
        continue

    for i in range(len(word) - 1): 
        if int(word[i], 16) % 2 == 0 and int(word[i + 1], 16) % 2 == 0:
            j = True 
            break

        if int(word[i], 16) % 2 != 0 and int(word[i + 1], 16) % 2 != 0: 
            j = True
            break
    
    if j: 
        continue

    res += 1

print(res)

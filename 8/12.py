"""
Сколько существует шестнадцатеричных трёхзначных чисел, в которых все цифры 
различны и никакие две чётные или две нечётные цифры не стоят рядом?
"""
import itertools
c = 0

for i in itertools.permutations('1234567890ABCDEF', r=3): 
    k = 0
    word = ''.join(i)

    if word[0] == '0': 
        continue
    

    for j in range(0, 2): 
        if int(word[j], 16) % 2 == int(word[j + 1], 16) % 2: 
            continue 

    c += 1

print(c)
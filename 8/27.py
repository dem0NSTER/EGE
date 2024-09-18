from itertools import product
c = 0

for i in product('пуля', repeat=6): 
    word = ''.join(i)
    if word.count('у') == 2: 
        c += 1

print(c)
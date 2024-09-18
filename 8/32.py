from itertools import product

c = 0

for i in product('вишня', repeat=6): 
    word = ''.join(i)
    if word.count('в') > 1: 
        continue
    if word[0] == 'ш': 
        continue
    if word[-1] in 'ия': 
        continue
    c += 1

print(c)
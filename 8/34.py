from itertools import product

c = 0

for i in product('гепард', repeat=5): 
    word = ''.join(i)
    if word.count('г') != 1: 
        continue
    if word[0] == 'а': 
        continue
    if word[-1] == 'е': 
        continue
    c += 1

print(c)
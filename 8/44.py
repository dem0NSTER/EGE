from itertools import product

c = 0
for i in product('абвгдя', repeat=5): 
    word = ''.join(i)
    if word.count('я') == 3: 
        c += 1

print(c)

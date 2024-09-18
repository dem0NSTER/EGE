from itertools import product

c = 0

for i in product('лодка', repeat=4): 
    word = ''.join(i)
    if word.count('о') > 1: 
        c += 1

print(c)

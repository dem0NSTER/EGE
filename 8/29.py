from itertools import product

c = 0

for i in product('сало', repeat=6): 
    if i.count('о') > 0: 
        if i.count('о') < 4: 
            c += 1

print(c)
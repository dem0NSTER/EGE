from itertools import product

c = 0
for i in product('abcdef', repeat=3): 
    print(i)
    c += 1

print(c)

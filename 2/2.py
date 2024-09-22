from itertools import product

print('a b,c')

for a, b, c in product([0, 1], repeat=3): 
    f = (a and not(c)) or (not(b) and not(c))
    if f == 1: 
        print(a, b, c)
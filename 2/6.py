from itertools import product

print('x z y w')

for z, x, y, w in product([0, 1], repeat=4): 
    f = (x and not(y)) or (x == z) or w
    if f == 0: 
        print(x, z, y, w)
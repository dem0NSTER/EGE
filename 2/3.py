from itertools import product

print('x y z')

for x, y, z in product([0, 1], repeat=3): 
    f = (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z))
    if f == 1: 
        print(x, y, z)
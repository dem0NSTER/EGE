from itertools import product

print('x y z')

for x, y, z in product([0, 1], repeat=3): 
    f = not(x == (y <= z))
    print(x, y, z, f)
from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4): 
    f = (x == (not(z))) <= ((x or w) == y)
    if f == 0: 
        print(x, y, z, w)
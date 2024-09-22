from itertools import product 

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4): 
    f = ((w <= y) or not(y <= z)) and not(x) and not(x == z)
    if f == 1: 
        print(x, y, z, w)
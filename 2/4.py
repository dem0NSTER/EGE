from itertools import product 

print('x y z w')

for x, y, z, w in product([0, 1], repeat=4): 
    f = ((not(x) and y) == z) and w
    if f == 1: 
        print(x, y, z, w)
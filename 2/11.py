from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4): 
    f = (y <= x) or not((x <= z) and (z <= x)) and not(w)
    if f == 0: 
        print(x, y, z, w)
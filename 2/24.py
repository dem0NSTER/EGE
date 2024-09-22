from itertools import product, permutations 

def f(x, y, w, z): 
    return ((y <= x) or (not(z) and w)) == (w == x)


for x in product([1, 0], repeat=3): 
    table = [
        (x[0], 1, 0, 0), 
        (0, 0, 0, 1), 
        (0, 1, x[1], x[2]), 
    ]
    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
            print(i)
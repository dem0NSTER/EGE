from itertools import permutations, product

def f(x, y, z, w): 
    return (x or y) and (not (y == z)) and (not w)


for a1, a2, a3, a4 in product([1, 0], repeat=4): 
    table = [
        (a1, 1, a2, 1), 
        (0, 0, 1, a3), 
        (0, a4, 1, 1)
    ]
    if len(table) != len(set(table)): 
        continue
    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
            print(i)
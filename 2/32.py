from itertools import product, permutations

def f(x, y, z, w): 
    return (z == (w<=x))<=y

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [
        (0, 0, 1, a1), 
        (a2, 0, 1, 1), 
        (0, 1, a3, a4)
    ]
    if len(table) != len(set(table)): 
        continue
    for j in permutations('xyzw'): 
        if [f(**dict(zip(j, row))) for row in table] == [0, 0, 0]: 
            print(*j, sep='')
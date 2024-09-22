from itertools import product, permutations 

def f(x, y, z, w):
    return (x == (not(y))) <= ((x and w) == z)


for i in product([0, 1], repeat=5): 
    table = [
        (1, 1, i[0], i[1]),
        (1, 1, i[2], 1),
        (i[3], 1, 1, i[4]),
    ]
    if len(table) != len(set(table)): 
        continue
    for j in permutations('xywz'): 
        if [f(**dict(zip(j, row))) for row in table] == [0, 0, 0]: 
            print(*j, sep='')
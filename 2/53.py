from itertools import product, permutations


def f(x, y, z, w): 
    return (not (x <= y)) or (z <= w) or (not z)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7): 
    table = [
        (a1, 0, a2, 0),
        (1, a3, a4, a5), 
        (0, 1, a6, a7)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(*i, sep='')

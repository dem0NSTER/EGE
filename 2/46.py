from itertools import product, permutations


def f(x, y, z, w): 
    return (x or (not y)) and ((not (x == z))) and w


for a1, a2, a3, a4 in product([0, 1], repeat=4): 
    table = [
        (a1, a2, 0, 0), 
        (1, 0, 0, 1),
        (1, 0, a3, a4)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
            print(*i, sep='')
            
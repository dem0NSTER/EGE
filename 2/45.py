from itertools import product, permutations


def f(x, y, z, w): 
    return ((not x) and (not y)) or (y == z) or (not w)


for a1, a2, a3, a4 in product([0, 1], repeat=4): 
    table = [
        (a1, 0, a2, 0), 
        (0, a3, 1, a4), 
        (1, 1, 1, 0)
    ]

    if len(table) != len(set(table)):
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]:
            print(*i, sep='')

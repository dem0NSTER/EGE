from itertools import product, permutations


def f(z, y, x, w): 
    return ((not z) == (not y)) or ((not x) and y) or w


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7): 
    table = [
        (a1, 1, a2, 1), 
        (1, 1, a3, a4), 
        (1, a5, a6, a7),
    ]

    if len(set(table)) != len(table): 
        continue

    for i in permutations('zywx'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(*i, sep='')
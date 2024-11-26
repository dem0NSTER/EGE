from itertools import product, permutations


def f(x, y, z, w): 
    return (not(z and (not w))) or ((z <= w) == (x <= y))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6): 
    table = [
        (1, a1, a2, a3), 
        (1, 1, a4, 1), 
        (1, a5, a6, 1)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(*i, sep='')

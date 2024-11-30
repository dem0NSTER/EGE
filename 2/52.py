from itertools import permutations, product


def f(x, y, z): 
    return (x == (not y)) or ((not x) <= z)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6): 
    table = [
        (0, a1, a2), 
        (a3, 0, a4),
        (a5, a6, 1)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyz'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 1, 0]: 
            print(*i, sep='')

# 23
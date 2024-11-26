from itertools import permutations, product


def f(w, z, y, x): 
    return (x == (not z)) <= ((x or w) == y)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5): 
    table = [
        (0, a1, 0, a2), 
        (a3, a4, 0, 0), 
        (a5, 0, 0, 0)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(*i, sep='')
            
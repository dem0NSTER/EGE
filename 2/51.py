from itertools import permutations, product


def f(x, y, w, z): 
    return (y <= x) and (not w) and z


for a1, a2, a3, a4 in product([0, 1], repeat=4): 
    table = [
        (1, 0, 1, 1), 
        (1, 0, a1, 1), 
        (a2, a3, a4, 1)
    ]

    if len(table) != len(set(table)): 
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
            print(*i, sep='')
            
from itertools import permutations, product 


def f(x, y, z, w): 
    return (w <= (y == z)) and (y == (z <= x))


for a1, a2 in product([0, 1], repeat=2): 
    table = [
        (a1, 0, 0, 0), 
        (0, a2, 1, 1), 
        (0, 0, 0, 1)
    ]

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 0]: 
            print(*i, sep='')

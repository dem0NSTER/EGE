from itertools import product, permutations

def f(x, y, z, w): 
    return (x and (not y)) or (x == z) or (not w)


for a1, a2, a3, a4 in product([1, 0], repeat=4): 
    table = (
        (a1, a2, 0, 0), 
        (1, 1, 1, 0), 
        (1, 0, a3, a4)
    )
    if len(set(table)) != len(table): 
        continue
    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(i)
            
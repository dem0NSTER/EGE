from itertools import permutations, product 

def f(x, y, z, w): 
    return ( ( (not(x)) <= (not(z)) ) and y ) <= ( (not(w)) <= (not(y)) )


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6): 
    table = [
        (1, 1, 1, a1), 
        (a2, a3, 1, a4), 
        (1, a5, 0, a6)
    ]
    if len(table) != len(set(table)):
        continue

    for i in permutations('xyzw'): 
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
            print(*i, sep='')
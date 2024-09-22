from itertools import permutations, product 

def f(x, y, z, w): 
    return x and (y <= z) or w

d = set()
for i in product([0, 1], repeat=6): 
    table = [
        (1, 0, i[0], 1),
        (i[1], 0, 1, i[2]),
        (i[3], 0, i[4], i[5]),
    ]
    if len(table) != len(set(table)): 
        continue

    for j in permutations('xyzw'): 
        if [f(**dict(zip(j, row))) for row in table] == [0, 0, 0]:
            d.add(j)
print(d, len(d))

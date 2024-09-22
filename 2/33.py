from itertools import permutations

def f(x, y, z, w): 
    return x and ((not y) and z and (not w) or y and (not z))


table = [ 
    (0, 1, 0, 1), 
    (0, 1, 1, 0), 
    (1, 1, 0, 1)
]

for i in permutations('xyzw'): 
    if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
        print(*i, sep='')
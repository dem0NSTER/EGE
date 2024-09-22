from itertools import permutations 

def f(x, y, z, w): 
    return not(y) or x or (not(z) and w)


table = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
]

for i in permutations('xyzw'): 
    if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
        print(i)
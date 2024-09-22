from itertools import permutations

def f(x, y, z, w): 
    return (y or x) == ((y <= w) or (not(z)))


table = [ 
    [1, 0, 0, 0], 
    [0, 1, 0, 0], 
    [1, 0, 1, 0], 
]

for i in permutations('xyzw'): 
    if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]: 
        print(i)
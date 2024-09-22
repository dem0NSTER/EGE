from itertools import permutations 

def f(x, y, z, w): 
    return (x == y) <= (z == w)


table = [
    (0, 0, 0, 1), 
    (1, 1, 1, 0), 
]

c = 0

for i in permutations('xyzw'): 
    if [f(**dict(zip(i, row))) for row in table] == [0, 0]: 
        c += 1
        print(i, c)
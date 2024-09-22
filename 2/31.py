from itertools import permutations

def f(x, y, z): 
    return (y <= z) and (x <= y)


table = [ 
    (1, 0, 0),
    (1, 0, 1),
]

for i in permutations('xyz'): 
    if [f(**dict(zip(i, row))) for row in table] == [1, 0]:
        print(*i, sep='')
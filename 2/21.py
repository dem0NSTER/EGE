from itertools import permutations

def f(a: dict): 
    x = a.get('x')
    y = a.get('y')
    z = a.get('z')
    return (not(x) and y and z) or (not(x) and not(z))

table = [
    [0, 0, 0], 
    [1, 0, 0],
    [1, 1, 0]
]

for i in permutations('xyz'): 
    if [f(dict(zip(i, row))) for row in table] == [1, 1, 1]: 
        print(i)
from itertools import permutations

def f(a, b, c): 
    return (a or (not c)) and ((not a) or b or c)


table = [
    (0, 0, 0), 
    (0, 0, 1), 
    (0, 1, 0), 
    (0, 1, 1), 
    (1, 0, 0), 
    (1, 0, 1), 
    (1, 1, 0), 
    (1, 1, 1), 
]

for i in permutations('abc'):
    if [f(**dict(zip(i, row))) for row in table] == [1, 0, 1, 1, 0, 1, 0, 1]:
        print(i)


from itertools import permutations 

def f(a, b, c, d): 
    return (a <= d) and not(b <= c)


table = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 0],
]

for i in permutations('abcd'): 
    if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]: 
        print(i)
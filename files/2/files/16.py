from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(5000)

@lru_cache(None)
def f(x, y): 
    if x == 0: 
        return y + 1
    if y == 0: 
        return f(x - 1, 1)
    return f(x - 1, f(x, y - 1))


for x in range(1, 3): 
    for y in range(1, 11): 
        f(x, y)

print(f(3, 2))

from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int: 
    if n == 1: 
        return 1
    if n > 1: 
        return f(n - 1) - 2 * g(n - 1)


@lru_cache(None)
def g(n: int) -> int: 
    if n == 1: 
        return 1
    if n > 1: 
        return f(n - 1) + g(n - 1) + n
    
num = g(36)
print(sum([int(i) for i in str(num)]))


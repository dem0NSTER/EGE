from functools import lru_cache


@lru_cache(None)
def f(n: int): 
    if n == 1: 
        return 2
    if n > 1: 
        return 2 * f(n - 1)
    
for n in range(1, 1900): 
    f(n)

print(f(1900) / 2**1890)
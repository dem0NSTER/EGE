from functools import lru_cache
from sys import set_int_max_str_digits

set_int_max_str_digits(100000)

@lru_cache(None)
def fac(n: int): 
    if n == 1: 
        return 1
    if n > 1: 
        return n * fac(n - 1)
    

for i in range(1, 5000): 
    fac(i)


@lru_cache(None)
def f(n: int): 
    if n >= 5000: 
        return fac(n)
    if 1 <= n < 5000: 
        return 2 * f(n + 1) // (n + 1)
    

for n in range(5000, 1, -1): 
    f(n)

print(1000 * f(7) / f(4))

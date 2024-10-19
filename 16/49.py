import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

def fuc(n: int) -> int: 
    if n == 1: 
        return 1
    if n > 1: 
        return n * fuc(n - 1)


# @lru_cache(None)
def f(n: int): 
    if n >= 5000: 
        return 10**9
    else: 
        return 2 * f(n + 1) / (n + 1)
    
print(f(7), f(4))
# print(1000 * f(7) / f(4))

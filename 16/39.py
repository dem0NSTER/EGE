from functools import lru_cache


# @lru_cache(None)
def f(n: int) -> int: 
    global s
    s.append('*')
    if n >= 1: 
        s.append('*')
        f(n - 1)
        f(n - 3)
        s.append('*')

s = []
f(40)
print(len(s))
import sys
sys.setrecursionlimit(2500)


def f(n: int) -> int: 
    if n == 1: 
        return 1
    if n > 1: 
        return n + f(n - 1)
    

print(f(2021) - f(2019))

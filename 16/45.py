import sys
sys.setrecursionlimit(100000)

def f(n: int) -> int: 
    if n > 100_000: 
        return n 
    if n <= 100_000: 
        return f(n + 1) + 5 * n + 2


print(f(3) - f(7))
import sys

sys.setrecursionlimit(1000000)

def f(n): 
    if n == 1: 
        return 1
    else: 
        return n * f(n - 1)

print(f(2222) / f(2219))
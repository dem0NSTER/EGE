import sys

sys.setrecursionlimit(10000)

def f(n: int):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

s = (2 * f(2024) + f(2023)) / f(2022)

print(s)
    

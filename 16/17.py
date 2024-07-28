import sys

sys.setrecursionlimit(2599)

def f(n: int): 
    if n == 1: 
        return 1
    if n > 1: 
        return n - 1 + f(n - 1)
    
print(f(2028) - f(2024))
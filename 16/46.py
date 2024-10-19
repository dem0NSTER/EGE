import sys 
sys.setrecursionlimit(20000)

def f(n: int): 
    if n <= 3: 
        return 3
    if n > 3 and n % 2 != 0: 
        return 2 * n + f(n - 2)
    if n > 3 and n % 2 == 0: 
        return n ** 2 + f(n - 1)
    
print(f(10_000) - f(9_995))

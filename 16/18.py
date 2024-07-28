def f(n: int): 
    if n == 1: 
        return 3
    if n % 2 == 0 and n > 1: 
        return f(n - 1) + n * 2
    if n % 2 != 0 and n > 1: 
        return 2 * f(n - 2) + n ** 2
    
print(f(n=64))
def f(n): 
    if n == 1: 
        return 1
    else: 
        return 2 * g(n) + 3 * n


def g(n): 
    if n == 1: 
        return 1
    else: 
        return f(n - 1) + 5 * n
    
print(f(4)-g(5))

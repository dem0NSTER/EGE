def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n > finish: 
        return 0
    if n < finish: 
        if n == 1: 
            return f(n + 1, finish) + f(n * 3, finish) + f(n + n, finish)
        else: 
            return f(n + 1, finish) + f(n * 3, finish) + f(n + (n - 1), finish)
        
print(f(1, 15))
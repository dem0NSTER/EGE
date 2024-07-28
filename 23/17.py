def f(n, finish): 
    if n == finish: 
        return 1 
    if n > finish or n == 22: 
        return 0
    if n < finish: 
        return f(n + 1, finish) + f(n + 2, finish) + f(n * 3, finish)
    
print(f(14, 29))

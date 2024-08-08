def f(n: int, finish: int, mult): 
    if n == finish: 
        return 1
    if n > finish or mult > 2: 
        return 0
    if n < finish: 
        return f(n + 3, finish, mult) + f(n * 4, finish, mult + 1) + f(n * 5, finish, mult+1)
    
print(f(5, 200, 0))

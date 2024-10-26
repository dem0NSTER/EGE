def f(n, finish): 
    if n == finish: 
        return 1
    if n > finish or n == 43: 
        return 0
    if n < finish: 
        return f(n + 2, finish) + f(n + (n - 1), finish) + f(n + (n + 1), finish)
    

print(f(7, 63))
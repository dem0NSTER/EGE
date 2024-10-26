def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n > finish: 
        return 0
    if n < finish: 
        return f(n + 1, finish) + f(n * 2, finish) + f(n * 2 + 1, finish) + f(n * 10, finish)
    

print(f(1, 15))

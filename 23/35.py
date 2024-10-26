def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n < finish: 
        return 0
    if n > finish: 
        return f(n - 8, finish) + f(n // 2, finish)


print(f(102, 43) * f(43, 5))

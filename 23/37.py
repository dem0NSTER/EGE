def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n > finish or n == 11 or n == 18: 
        return 0
    if n < finish: 
        return f(n + 1, finish) + f(n + 2, finish) + f(n * 3, finish)


print(f(4, 8) * f(8, 23))

def f(n: int, finish: int): 
    if n == finish: return 1
    if n < finish: return 0
    if n > finish: return f(n - 1, finish) + f(n - 3, finish) + f(n // 3, finish)


print(f(22, 2))

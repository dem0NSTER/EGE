def f(n, finish: int): 
    if n == finish: return 1
    if n > finish or n == 512: return 0
    if n < finish: return f(n + 2, finish) + f(n * 3, finish)

print(f(6, 54) * f(54, 1006))

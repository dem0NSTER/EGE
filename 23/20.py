def f(n, finish): 
    if n == finish: return 1
    if n > finish or n == 41: return 0
    if n < finish: return f(n + 3, finish) + f(n * 2, finish) + f(n ** 2, finish)

print(f(5, 68) * f(68, 169))
def f(n, finish): 
    if n == finish: 
        return 1
    if n < finish or n == 5: return 0
    if n > finish: return f(n - 1, finish) + f(n - 3, finish) + f(n // 3, finish)


print(f(29, 12) * f(12, 3))

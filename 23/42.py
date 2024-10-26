def f(n: int, finish: int): 
    if n == finish: return 1
    if n > finish: return 0
    if n < finish and n % 2 == 0: 
        return f(n + 1, finish) + f(n * 1.5, finish)
    if n < finish and n % 2 != 0: 
        return f(n + 1, finish)


print(f(1, 20))
    
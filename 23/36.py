def f(n, finish):
    if n == finish: 
        return 1
    if n > finish or n == 6: 
        return 0
    if n < finish: 
        return f(n + 2, finish) + f(n * 3, finish)
    

print(f(1, 25) * f(25, 63))

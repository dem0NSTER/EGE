def f(n: int, finish: int): 
    if n == finish: return 1
    if n > finish: return 0
    if n < finish: return f(n + 2, finish) + f(n + 4, finish) + f(n + 5, finish)


for i in range(32, 1000): 
    if f(31, i) == 1001: 
        print(i)
        break
    
def f(n: int, finish: int, commands): 
    if n == finish and commands == 7: return 1
    if n == finish and commands != 7: return 0
    if n > finish: return 0
    if n < finish: return f(n + 1, finish, commands + 1) + f(n + 4, finish, commands + 1) + f(n * 2, finish, commands + 1)

print(f(3, 27, 0))
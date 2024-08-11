def f(n:int, finish: int, mult:int):
    if n == finish: return 1
    if n > finish or mult > 2 or n == 8: return 0
    if n < finish:
        return f(n + 1, finish, mult) + f(n + 2, finish, mult) + f(n * 2, finish, mult+1)

print(f(1, 24, 0))

def f(n, finish):
    if n == finish:
        return 1
    if n < finish:
        return 0
    if n > finish:
        return f(n - 1, finish) + f(n // 2, finish)

print(f(30, 8) * f(8, 1))

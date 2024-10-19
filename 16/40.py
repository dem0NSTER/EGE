def f(n: int) -> int: 
    global s 
    s.append(n * n)
    if n > 1: 
        s.append(2 * n + 1)
        f(n - 2)
        f(n // 3)


s = []
f(100)
print(sum(s))
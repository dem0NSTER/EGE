def f(n: int) -> int: 
    if n == 1: 
        return 1
    if n == 2: 
        return 2
    if n > 2 and n % 2 == 0: 
        return int((n + f(n - 2)) / 5)
    if n > 2 and n % 2 != 0: 
        return int((2 * n + f(n - 1) + f(n - 2)) / 4)

print(f(50))
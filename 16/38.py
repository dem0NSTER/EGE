def f(n: int) -> int: 
    if n == 1: 
        return 1
    if n > 1 and n % 2 == 0: 
        return f(n / 2) + 1
    if n > 1 and n % 2 != 0: 
        return f(n - 1) + n

for n in range(1, 1000): 
    if f(n) == 19:
        print(n)
        break

def f(n: int) -> int: 
    if n > 30: 
        return n ** 2 + 5 * n + 4
    if n <= 30 and n % 2 == 0: 
        return f(n + 1) + 3 * f(n + 4)
    if n <= 30 and n % 2 != 0: 
        return 2 * f(n + 2) + f(n + 5)


c = 0
for n in range(1, 1000 + 1): 
    n1 = f(n)
    num = [int(i) for i in str(n1)]
    if sum(num) == 27: 
        c += 1

print(c)

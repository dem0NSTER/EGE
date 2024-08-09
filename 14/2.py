def f(n: int, base: int) -> str: 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

s = 9 ** 8 * 3 ** 20 - 3 ** 10 - 3
print(f(s, 3).count('2'))
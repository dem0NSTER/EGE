def f(n: int, base: int) -> str: 
    s = ''

    while n != 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

ss = 49 ** 7 + 7 ** 21 - 7
print(f(ss, 7).count('6'))

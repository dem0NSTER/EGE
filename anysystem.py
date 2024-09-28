def anysystem(n: int, base: int) -> str: 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


print(anysystem(2, 2))
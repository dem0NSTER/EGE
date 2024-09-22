def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


a = 6 * 144**26 + 11 * 12**75 - 48
b = f(a, 12)
print(b.count(11))
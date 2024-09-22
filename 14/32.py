def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024
b = f(a, 25)
print(b.count(0))

def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]

a = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
b = f(a, 15)
print(len(set(b)))
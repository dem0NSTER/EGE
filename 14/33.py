def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]



for x in range(1, 100): 
    a = 36**17 - 6**x + 71
    b = f(abs(a), 6)
    if sum(b) == 61: 
        print(x)
        break
def f(n, base): 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

for x in range(20, 31): 
    b = f(x, 3)
    if b[-2::] == '11': 
        print(x)
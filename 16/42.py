def f(n: int) -> int: 
    if n < 3: 
        return n + 1
    if n >= 3 and n % 2 == 0: 
        return f(n - 2) + n - 2
    if n >= 3 and n % 2 != 0: 
        return f(n + 2) + n + 2


c = 0
for n in range(1, 10000): 
    try: 
        num = f(n)
        if len(str(num)) == 5: 
            c += 1
    except RecursionError: 
        continue

print(c)

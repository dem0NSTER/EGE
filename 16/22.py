def f(n): 
    if n < 5: 
        return n 
    if n % 7 == 0: 
        return f(n // 7) + 15*n
    else: 
        return f(n + 14) + n
    
for i in range(1, 1000): 
    try:
        if f(i) > 399: 
            print(i)
            break
    except RecursionError: 
        continue
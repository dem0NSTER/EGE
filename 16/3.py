def f(n): 
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    
    elif n > 1 and n % 2 == 0: 
        return 2 + int(3 * f(n - 1) / 3)
    
    elif n > 1 and n % 2 != 0: 
        return 2 * n + int((f(n - 1) + f(n - 3) + 2) / 3)
    

print(f(30))

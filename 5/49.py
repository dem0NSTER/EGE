c = 0

for n in range(2, 10000): 
    if n % 3 == 0: 
        n = n / 3
    else: 
        n = n - 1
    
    if n % 5 == 0: 
        n = n / 5
    else: 
        n = n - 1
    
    if n % 11 == 0: 
        n = n / 11
    else: 
        n = n - 1
    
    if n == 8: 
        c += 1
    
print(c)
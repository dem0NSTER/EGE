def F(n):
    if n == 0: 
        return 0
    elif n > 0 and n % 2 == 0: 
        return F(n/2)
    else: 
        return 1 + F(n-1)
    
for i in range(11200): 
    if F(i) == 12: 
        print(i)
        break

print(F(12))

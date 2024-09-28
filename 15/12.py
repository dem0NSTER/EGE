def f(x, a): 
    return (x % a != 0) <= ((x % 36 == 0) <= (x % 54 != 0))


for a in range(1000, 1, -1): 
    if all(f(x, a) for x in range(1000)): 
        print(a)
        break
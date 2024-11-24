def f(x, a): 
    return (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


for a in range(1000, 1, -1): 
    if all(f(x, a) for x in range(1, 1000)): 
        print(a)
        break
    
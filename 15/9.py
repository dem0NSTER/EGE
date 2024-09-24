def f(x, a): 
    return ((x & 84 != 0) or (x & 66 != 0)) <= ((x & 51 == 0) <= (x & a != 0))


for a in range(0, 1000): 
    if all(f(x, a) for x in range(1, 1000)): 
        print(a)
        break
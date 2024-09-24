def f(x, a): 
    return (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))


for a in range(1000, 0, -1): 
    if all(f(x, a) for x in range(10000)): 
        print(a)
        break
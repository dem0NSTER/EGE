def f(y, x, a): 
    return (2*y + 5*x != 17) or (a > 2*x + 3*y) and (a > 4*y + x + 1)


for a in range(-500, 500): 
    if all(f(y, x, a) for y in range(1000) for x in range(1000)): 
        print(a)
        break
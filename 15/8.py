def f(x, y, a): 
    return ((x < 8) <= ((x * x) < a)) and (((y * y) <= a) <= (y < 10))

c = 0
for a in range(-1000, 500):
    if all(f(x, y, a) for x in range(100) for y in range(100)): 
        c += 1

print(c)

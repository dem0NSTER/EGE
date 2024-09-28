def f(x, a): 
    p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    return ((x in a) <= (x in p)) and ((x in q) <= (not x in a))


a = set(range(1000))

for x in range(-1000, 1000): 
    if not f(x, a): 
        a.remove(x)

print(len(a))
res = []

for n in range(1, 1000): 
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    r = int(n2, 2)
    if r < 80: 
        res.append(r)

print(len(res))
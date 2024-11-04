res = []

for n in range(5, 10000): 
    n1 = n - bin(n)[2:].count('0')
    n2 = bin(n1)[2:]
    n2 = n2[-3:] + n2
    r = int(n2, 2)
    if r > 224: 
        res.append(r)

print(min(res))

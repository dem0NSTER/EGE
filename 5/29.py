res = []

for n in range(1, 1000): 
    n2 = bin(n)[2:]
    if n % 2 == 0: 
        n2 += '01'
    else: 
        n2 += '10'

    r = int(n2, 2)
    if r > 81: 
        res.append(r)

print(min(res))
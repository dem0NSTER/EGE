from itertools import product

res = []
for i in product('солнце', repeat=6):
    word = ''.join(i)
    res.append(word)

res.sort()

c = 0
for i in range(len(res)): 
    if (i + 1) % 2 == 0: 
        if res[i][0] in 'слнц': 
            if res[i].count('ц') == 2: 
                c += 1

print(c)

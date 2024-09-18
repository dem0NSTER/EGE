from itertools import product

res = []

for i in product('мария', repeat=4): 
    word = ''.join(i)
    res.append(word)

res.sort()

print(res.index('ария') + 1)
from itertools import product

res = []

for i in product('алгоритм', repeat=4): 
    word = ''.join(i)
    res.append(word)

res.sort(reverse=True)

for i in res: 
    if i[-2:] == 'им': 
        res.sort()
        print(i)
        print(res.index(i) + 1)
        break
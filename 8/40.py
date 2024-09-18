from itertools import product

res = []

for i in product('лемур', repeat=4): 
    word = ''.join(i)
    res.append(word)

res.sort()

for i in res: 
    if i[0] == 'л': 
        print(i)
        print(res.index(i) + 1)
        break

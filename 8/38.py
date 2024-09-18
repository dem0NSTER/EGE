from itertools import permutations

res = []

for i in permutations('мимикрия', r=8):
    word = ''.join(i)
    res.append(word)

print(len(res), len(set(res)))
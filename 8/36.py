from itertools import permutations

c = 0

for i in permutations('дейкстра', r=6): 
    word = ''.join(i)
    if word.count('й') == 1: 
        index = word.index('й')
        if index == 5:
            continue
        if word[index + 1] in 'дйкстр': 
            c += 1

print(c)
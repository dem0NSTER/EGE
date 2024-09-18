from itertools import permutations

c = 0 

for i in permutations('вайфу', r=4): 
    word = ''.join(i)
    if word[0] == 'й': 
        continue
    if word.count('вф') + word.count('фв') != 0: 
        continue
    c += 1

print(c)
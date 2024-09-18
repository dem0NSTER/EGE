from itertools import permutations

c = 0

for i in permutations("игрок", r=5): 
    word = ''.join(i)
    if word[0] == 'к': 
        continue
    if 'рок' in word: 
        continue
    c += 1 

print(c)
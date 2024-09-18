from itertools import product

c = 0

for i in product('abcd', repeat=4):
    word = ''.join(i)
    word_2 = ''.join(sorted(i))

    if word == word_2: 
        c += 1

print(c)

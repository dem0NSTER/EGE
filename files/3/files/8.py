from itertools import product

c = 0
for i in product('01234567', repeat=5):
    word = ''.join(i)
    if word[0] in '01357':
        continue
    if word[-1] in '26':
        continue
    if word.count('7') > 2:
        continue
    c += 1

print(c)

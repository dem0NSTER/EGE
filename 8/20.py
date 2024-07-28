"""
Сколько существует девятеричных пятизначных чисел, которые содержат в 
своей записи 
ровно две цифры 3, в которых нечетная цифра не стоит рядом с цифрой 2?
"""

import itertools 

c = 0

for i in itertools.product('012345678', repeat=5): 
    not_ = False
    word = ''.join(i)

    if word[0] == '0': 
        continue

    if word.count('3') != 2:
        continue

    index_2 = []
    for i in range(len(word)): 
        if word[i] == '2':
            index_2.append(i)

    for i in index_2: 
        if i == 0: 
            if int(word[i + 1], 9) % 2 != 0:
                not_ = True
                break
            
        elif i == 4: 
            if int(word[i - 1], 9) % 2 != 0: 
                not_ = True
                break

        else: 
            if int(word[i + 1], 9) % 2 != 0 or int(word[i - 1], 9) % 2 != 0: 
                not_ = True
                break

    if not_: 
        continue

    c += 1
    

print(c)
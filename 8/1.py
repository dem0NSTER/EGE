"""
Определите количество пятизначных чисел, записанных в шестнадцатеричной системе счисления, 
в записи которых ровно одна цифра 4, при этом никакая нечётная цифра не стоит рядом с цифрой 4.
"""
import itertools

alphabit = '0123456789abcdef'
count = 0 

for i in itertools.product(alphabit, repeat=5):
    word = ''.join(i)
    if word.count("4") != 1: 
        continue
    
    index_4 = word.index('4')

    if index_4 == 0: 
        if int(word[index_4 + 1], 16) % 2 != 0: 
            continue

    elif index_4 == 4: 
        if int(word[index_4 - 1], 16) % 2 != 0: 
            continue

    else: 
        if int(word[index_4 + 1], 16) % 2 != 0 or int(word[index_4 - 1], 16) % 2 != 0: 
            continue

    count += 1

print(count)

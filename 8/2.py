"""
Сколько существует пятизначных чисел, записанных в восьмеричной системе счисления, 
в записи которых присутствует хотя бы одна пара одинаковых элементов, стоящих рядом?
"""
import itertools

count = 0

for i in itertools.product('01234567', repeat=5): 
    word = ''.join(i)

    if word[0] == '0': 
        continue

    for i in range(0, len(word) - 1): 
        if word[i] == word[i + 1]: 
            count += 1
            break


print(count)
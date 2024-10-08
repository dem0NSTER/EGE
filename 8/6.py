"""
Все 6-буквенные слова, в составе которых могут быть буквы А, К, Р, М, Е, 
записаны в определённом порядке и пронумерованы, начиная с 1. Ниже приведено начало списка.
1. АААААА
2. АААААК
3. АААААР
4. АААААМ
5. АААААЕ
6. ААААКА
...  
Под каким номером в списке идёт слово “МАРКЕР”?
"""

import itertools
s = 'АКРМЕ'
c = 0

for i in itertools.product(s, repeat=6): 
    word = ''.join(i)
    c += 1
    if word == 'МАРКЕР': 
        break
print(c)

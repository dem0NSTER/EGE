def f(n: int, base: int): 
    new = ''
    while n > 0: 
        number = n % base
        new += str(number)
        n = n // base
    
    return new[::-1]

for n in range(1, 1000): 
    number = f(n, 2)
    if number.count('1') % 2 == 0: 
        number += '0'
    else: 
        number += '1'

    if number.count('1') % 2 == 0: 
        number += '0'
    else: 
        number += '1'
    if int(number, 2) > 120: 
        print(int(number, 2))
        break
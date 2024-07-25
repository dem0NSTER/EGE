def f(n: int, base: int) -> str: 
    new = ''

    while n > 0: 
        num = n % base
        new += str(num)
        n = n // 2

    return new[::-1]

res = []

def summ(n: int) -> int: 
    return sum(map(int, str(n)))

for n in range(1, 1000): 
    n2 = bin(n)[2:]

    if summ(n) % 2 == 1: 
        n2 += '1'
    else: 
        n2 += '0'

    if summ(int(n2, 2)) % 2 != 0: 
        n2 += '1'
    else: 
        n2 += '0'

    r = int(n2, 2)

    if r > 1234: 
        print(r)
        break


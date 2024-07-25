def f(n: int, base: int) -> str: 
    new = ''

    while n > 0: 
        num = n % base
        new += str(num)
        n = n // 2
    return new[::-1]


for n in range(1, 1000): 
    num = f(n, 2)
    if n % 2 == 0: 
        summ = num.count('1')
        num += bin(summ)[2:]

    else: 
        num = '1' + num + '00'

    r = int(num, 2)
    if r > 401: 
        print(n)
        break
    
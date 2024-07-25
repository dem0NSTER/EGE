def f(n: int, base: int) -> str: 
    new = ''

    while n > 0: 
        num = n % base
        new += str(num)
        n = n // 2
    
    return new[::-1]

res = []

for n in range(1, 1000): 
    num = f(n, 2)
    if n % 2 == 0: 
        num = '1' + num + '10'
    else: 
        num = '11' + num + '0'

    r = int(num, 2)

    if r > 130: 
        res.append(r)


print(min(res))
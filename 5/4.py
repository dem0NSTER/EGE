def f(n: int, base: int) -> str: 
    new = ''

    while n > 0:
        number = n % base
        new += str(number)
        n = n // 2
    return new[::-1]

res = []
def main(): 
    for n in range(1, 10000): 
        num = f(n, 2)
        if n % 2 == 0: 
            num = '1' + num
        else: 
            num += '0'
        
        if num.count('1') % 2 == 0: 
            num += '1'
        else: num += '0'
        
        if int(num, 2) > 300: 
            res.append(n)

main()
print(min(res))
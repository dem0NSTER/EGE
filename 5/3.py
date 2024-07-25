def f(n: int, base: int) -> str: 
    new = ''
    while n > 0: 
        number = n % 2
        new += str(number)
        n = n // 2
    return new[::-1]

def main(): 
    for n in range(1, 19000000): 
        number = f(n, 2)
        number += number[-1]
        if f(n, 2).count('1') % 2 == 0: 
            number += '0'
        else: 
            number += '1'

        number += '1'

        r = int(number, 2)
        if r > 553: 
            print(n)
            break

main()
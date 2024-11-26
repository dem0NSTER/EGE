def f(n: int, base: int): 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]


s = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023

s6 = f(s, 6)

print(s6.count('0'))

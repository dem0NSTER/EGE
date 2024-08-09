def f(n: int, base: int) -> str: 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

s = 81 ** 79 + 75 ** 2022 - 12 ** 35
s1 = f(s, 5)
res = 0

for i in range(len(s1) - 1): 
    if s1[i] == '4': 
        if s1[i + 1] == '1' or s1[i + 1] == '2'or s1[i + 1] == '3': 
            res += 1

print(res)  # 179

print(s1.count('41') + s1.count('42') + s1.count('43'))
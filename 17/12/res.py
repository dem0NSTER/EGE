with open('17-3.txt') as file:
    s1 = file.read().split('\n')

def f(n: int, base: int):
    s = []

    while n > 0:
        s.append(n % base)
        n = n // base
    return s[::-1]

s = [int(i) for i in s1]

max15 = '1e946'

max13 = 36669

res = []

for i in range(len(s) - 1):
    if (abs(s[i] - s[i + 1])) % 12 == 0:
        if (hex(s[i])[2:].count('e') == 2) or (hex(s[i + 1])[2:].count('e') == 2):
            print(abs(s[i] - s[i + 1]))
            print(hex(s[i]), hex(s[i + 1]))
            res.append(abs(s[i] - s[i + 1]))

print(len(res), min(res))
        

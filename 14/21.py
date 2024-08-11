def f(n: int, base: int):
    s = ''

    while n > 0:
        s += str(n % base)
        n = n // base
    return s[::-1]

n = 8**24 - 55 * 4 + 18**55
s = f(n, 4)
print(s)
c = 0

for i in range(len(s) - 1):
    g = s[i] + s[i + 1]
    if g == '21' or g == '22' or g == '23':
        c += 1
print(c)

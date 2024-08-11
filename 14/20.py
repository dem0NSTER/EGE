def f(n, base):
    s = []

    while n > 0:
        s.append(n % base)
        n = n // base
    return s[::-1]

s = 35**35 - 50**50 - 56**56 + 80**80
s1 = f(s, 7)

ctn = 0

for i in s1:
    if i % 2 == 0:
        ctn += 1

print(ctn)

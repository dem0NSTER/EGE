def f(n: int, base: int) -> str:
    s = []

    while n > 0:
        s.append(n % base)
        n = n // base
    return s[::-1]

s = 36 ** 8 + 6 ** 20 - 12
ctn = 0

for i in f(s, 6):
    if i == 5:
        ctn += 1

print(ctn)

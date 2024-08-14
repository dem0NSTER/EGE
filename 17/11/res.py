def f(n: int, base: int):
    s = ''

    while n > 0:
        s += str(n % base)
        n = n // base
    return s[::-1]

s = []
res = []

for i in range(99, 1000):
    s.append(i)

for i in s:
    if hex(i)[-1] == "9":
        if f(i, 9)[-1] == "8":
            res.append(i)


print(sum(res), len(res))
# 3558 6

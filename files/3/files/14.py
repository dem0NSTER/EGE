def f(n: int) -> str:
    s = ''

    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]

for x in range(2030, 1, -1):
    s = f(3 ** 100 - x)
    if s.count('0') == 5:
        print(x)
        break

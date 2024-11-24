def div(n: int):
    s = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)


c = 0
for n in range(800_001, 10**100):
    m = 0
    d = div(n)
    if len(d) > 0:
        m = min(d) + max(d)

    if str(m)[-1] == '4':
        print(n, m)
        c += 1

    if c == 5:
        break

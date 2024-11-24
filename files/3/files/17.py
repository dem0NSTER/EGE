s = [int(i) for i in open('17.txt')]

minn = min(s)

res = []
for i in range(len(s) - 1):
    if s[i] % 55 == minn or s[i + 1] % 55 == minn:
        res.append(s[i] + s[i + 1])

print(len(res), min(res))


with open('17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

maxs = -110000
res = []
for i in s:
    if i % 171 == 0 and i > maxs:
        maxs = i

for i in range(len(s) - 1):
    if (s[i] < maxs or s[i + 1] < maxs) and (s[i] % 2 == 0 or s[i + 1] % 2 == 0):
        res.append(s[i] + s[i + 1])

print(len(res), max(res)) # 7441 19643

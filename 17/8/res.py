with open('17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

mins = min(s)

res = []

for i in range(len(s) - 1):
    if (s[i] % 18) + (s[i + 1] % 18 ) == mins:
        res.append(s[i] + s[i + 1])

print(len(res), max(res))
# 285 166436

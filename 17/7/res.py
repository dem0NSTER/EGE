with open('17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

count32 = 0

for i in s:
    if i % 32 == 0:
        count32 += 1

res = []

for i in range(len(s) - 1):
    if ((s[i] < 0) + (s[i + 1] < 0)) > 0:
        if (s[i] + s[i + 1]) < count32:
            res.append(s[i] + s[i + 1])

print(len(res), max(res))     


# 4234 243
# 4234 243

with open('17Dosrok.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

mins = 110001
res = []

for i in s:
    if i % 23 == 0 and i < mins:
        mins = i
print(mins)

for i in range(len(s) - 1):
    if (s[i] % mins == 0 or s[i + 1] % mins == 0):
        res.append(s[i] + s[i + 1])

print(len(res), max(res)) # 18 15429



with open('17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


res = []
mins = 10 ** 100
for i in s:
    if i % 2 != 0:
        mins = min(mins, i)

for i in range(len(s) - 1):
    if ((s[i] % 3 == 0) + (s[i + 1] % 3 == 0)) == 1:
        if abs(s[i] - s[i + 1]) < mins:
            res.append(abs(s[i] - s[i + 1]))

print(len(res), max(res))
# 748 826



with open('17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

maxs = -10 ** 1000

for i in s:
    if str(i)[-2:] == '13':
        maxs = max(maxs, i)

print(min(s))
        
res = []

for i in range(len(s) - 2):
    if ((len(str(s[i])) == 3) + (len(str(s[i+1])) == 3) + (len(str(s[i+2])) == 3)) == 2:
        if (s[i] + s[i + 1] + s[i + 2]) <= maxs:
            res.append(s[i] + s[i + 1] + s[i + 2])

print(len(res), max(res))
# 959 97471

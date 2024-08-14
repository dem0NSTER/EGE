with open('2_17.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

mins = 100000000000003124
res = []

for i in s:
    if len(str(i)) == 3 and str(i)[-1] == '5' and i < mins:
        mins = i

for i in range(len(s) - 1):
    if (len(str(s[i])) == 3 or len(str(s[i + 1])) == 3):
        if not(len(str(s[i])) == 3 and len(str(s[i + 1])) == 3):
            if (s[i] + s[i + 1]) % mins == 0:
                res.append(s[i] + s[i + 1])
print(len(res), min(res)) # 12 375

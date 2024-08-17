with open('17-d10.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

sr = sum(s) / len(s)
sr2 = 2 * sr
res = []

for i in range(len(s) - 1):
    if (( hex(s[i]).count('f9') != 0 ) + ( hex(s[i + 1]).count('f9') != 0 )) == 2 \
       or (s[i] + s[i + 1]) < sr2:
        res.append(s[i] + s[i + 1])

print(len(res), max(res))

        

with open('17-d2.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

sr = sum(s) / len(s)
res = []

for i in range(len(s) - 1):
    if s[i] < sr or s[i + 1] < sr:
        if oct(s[i]).count('3') == 0 and oct(s[i + 1]).count('3') == 0:
            res.append(s[i] + s[i + 1])

print(len(res), min(res))

            

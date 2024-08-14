with open('17_1.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]
mins = min(s)
res = []

for i in range(len(s) - 2):
    if s[i] % 5 == 0 and s[i + 1] % 5 == 0 and s[i + 2] % 5 == 0:
        if s[i] % mins != 0 and s[i + 1] % mins != 0 and s[i + 2] % mins != 0:
            res.append(s[i] + s[i + 1] + s[i + 2])
            
print(len(res), max(res))

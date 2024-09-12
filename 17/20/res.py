with open(r'D:\Python_program\ege\17\20\17.txt') as file: 
    s1 = file.read().split('\n')

s = [int(x) for x in s1]
sr = sum(s) / len(s)
res = []

for i in range(len(s) - 1): 
    if (s[i] < sr) + (s[i + 1] < sr) > 0: 
        if (oct(s[i])[2:].count('3') == 0) + (oct(s[i + 1])[2:].count('3') == 0) == 2: 
            res.append(s[i] + s[i + 1])

print(len(res), min(res))

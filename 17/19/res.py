with open('17-3.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

"""12 e"""
res = []
print(hex(20))


for i in range(len(s) - 1):
    c = abs(s[i] - s[i + 1])
    if c % 12 == 0:
        if hex(s[i])[2:].count('e') == 2 or hex(s[i + 1])[2:].count('e') == 2:
            res.append(abs(s[i] - s[i + 1]))


print(len(res), min(res))

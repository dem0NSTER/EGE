with open('17/32/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(n, m): 
    return (n + m >= 100) and (n < 0 or m < 0)


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] * s[i + 1])

print(len(res), max(res))

with open('17/26/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(n: int, m: int): 
    return (n + m) % 3 == 0 and (n + m) % 6 != 0 and str(n * m)[-1] == '8'


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] + s[i + 1])

print(len(res), max(res))

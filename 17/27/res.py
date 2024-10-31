with open('17/27/1.txt') as file: 
    s1 = file.read().split('\n')


def f(n: int, m: int): 
    return n * m >= 0 and (n + m) % 7 == 0


s = [int(i) for i in s1]


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] * s[i + 1])

print(len(res), min(res))

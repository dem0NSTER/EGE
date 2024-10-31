with open('17/37/1.txt') as file: 
    s = [int(i) for i in file.read().split()]

res_4 = []
for i in s: 
    if str(i)[-1] == '4': 
        res_4.append(i)

min_max_4 = min(res_4) + max(res_4)


def f(n, m): 
    return n + m < min_max_4 


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] + s[i + 1])

print(len(res), max(res))

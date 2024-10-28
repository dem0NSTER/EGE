with open('17/24/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(n: int): 
    return n % 13 == 7 and n % 7 != 0 and n % 11 != 0


res = []
for i in s: 
    if f(i): 
        res.append(i)

print(max(res) - min(res), len(res))

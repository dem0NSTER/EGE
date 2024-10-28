with open('17/25/1.txt') as file: 
    s1 = file.read().split('\n')


s = [int(i) for i in s1]


def f(n: int): 
    return (hex(n)[-1] == 'b') and \
    (n % 7 == 0 and n % 6 != 0 and n % 13 != 0 and n % 19 != 0)


res = []
for i in s: 
    if f(i): 
        res.append(i)

print(sum(res), len(res))

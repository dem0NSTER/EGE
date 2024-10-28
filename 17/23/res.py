with open('17/23/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(n: int): 
    return (str(n)[-1] == '5' or str(n)[-1] == '7') and (n % 9 != 0 and n % 11 != 0)


res = []
for i in s:
    if f(i): 
       res.append(i)

print(len(res), max(res) + min(res))
 
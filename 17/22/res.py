with open('17/22/1.txt') as file: 
    a1 = file.read().split('\n')


s = [int(i) for i in a1]


def f(n: int): 
    return (str(n)[-1] == '2' or str(n)[-1] == '7') and (n % 3 == 0 and n % 11 == 0)


res = []
for num in s: 
    if f(num): 
        res.append(num)

print(len(res), min(res))

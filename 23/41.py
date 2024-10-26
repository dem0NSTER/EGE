def func(n: int): 
    num = [i for i in str(n)]
    num2 = []
    for i in num: 
        if i == '9': 
            num2.append('9')
        else: 
            num2.append(str(int(i) + 1))
    
    res = ''.join(num2)
    result = int(res)
    return result


def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n > finish: 
        return 0
    if n < finish: 
        return f(n + 1, finish) + f(func(n), finish)


print(f(25, 51))

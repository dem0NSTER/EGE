def func1(n: str): 
    return bin(int(n, 2) + 1)[2:]

def func2(n: str): 
    return n + '0'

def func3(n: str): 
    return n + '1'


def f(n: int, finish: int): 
    if int(n, 2) == int(finish, 2): 
        return 1
    if int(n, 2) > int(finish, 2): 
        return 0
    if int(n, 2) < int(finish, 2): 
        return f(func1(n), finish) + f(func2(n), finish) + f(func3(n), finish)
    

print(f('100', '11101'))


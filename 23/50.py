def f(n: int, finish: int, data: str): 
    if n > finish or data.count('1') > 1: 
        return 0
    if n == finish and data.count('1') == 1: 
        return 1
    if n == finish and data.count('1') != 1: 
        return 0
    if n < finish: 
        return f(n + 1, finish, data + f'{n % 2}') + f(n + 2, finish, data + f'{n % 2}') + f(n * 2, finish, data + f'{n % 2}')
    

print(f(2, 40, ''))

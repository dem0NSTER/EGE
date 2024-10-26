def f(n: int, finish: int, data: str): 
    if n > finish or data.count('0') > 6: 
        return 0
    if n == finish and data.count('0') == 6: 
        return 1
    if n == finish and data.count('0') != 6: 
        return 0
    if n < finish: 
        return f(n + 1, finish, data + f'{n % 2}') + f(n + 3, finish, data + f'{n % 2}') + f(n + 5, finish, data + f'{n % 2}')


print(f(3, 25, ''))
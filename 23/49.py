def f(n: int, finish: int, commands: str): 
    if n == finish and commands.count('*') <= 3: 
        return 1
    if n == finish and commands.count('*') > 3: 
        return 0
    if n > finish: 
        return 0
    if n < finish: 
        return f(n + 2, finish, commands + '+') + f(n * 3, finish, commands + '*') + f(n * 5, finish, commands + '*')
    

print(f(2, 200, ''))

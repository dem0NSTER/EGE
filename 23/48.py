def f(n, finish, commands): 
    if n == finish and commands.count('*') == 1: 
        return 1
    if n == finish and commands.count('*') != 1: 
        return 0
    if n > finish: 
        return 0
    if n < finish: 
        return f(n + 1, finish, commands + '+') + f(n + 2, finish, commands + '+') + f(n * 2, finish, commands + '*')
    

print(f(2, 12, ''))
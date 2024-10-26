def f(n: int, finish: int, comands: str):
    if n == finish and comands.count('**') == 0: 
        return 1
    if n == finish and comands.count('**') != 0: 
        return 0
    if n > finish: 
        return 0
    if n < finish: 
        return f(n + 1, finish, comands + '+') + f(n + 2, finish, comands + '+') + f(n * 2, finish, comands + '*')
    

print(f(1, 15, ''))

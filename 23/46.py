c = set()


def f(n: int, commands: int): 
    if commands == 8 and 1000 <= n <= 1024: 
        c.add(n)
    if commands > 8: 
        return 0
    else: 
        f(n + 1, commands + 1)
        f(n + 5, commands + 1)
        f(n * 3, commands + 1)


f(1, 0)
print(len(c))

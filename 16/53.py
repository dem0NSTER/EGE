res= []

def f(n): 
    res.append('*')
    if n >= 1: 
        res.append('*')
        f(n - 1)
        f(n - 2)

f(28)
print(len(res))

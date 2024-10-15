a = set()


for i in range(10000): 
    s = i * '5'
    while '555' in s or '888' in s: 
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    a.add(s)

print(a, len(a))
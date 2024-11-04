res = []
for i in range(100): 
    res.append(2 ** i)

for x in range(1000): 
 
    if int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8) in res: 
        print(x)
        break



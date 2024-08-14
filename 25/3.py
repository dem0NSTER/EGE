c = 0

for i in range(800000, 800000*1000):
    delet = [None]
    mins = 0
    maxs = 0
    for x in range(2, i): 
        if i % x == 0: 
            delet.append(x)
            
    if len(delet) > 1: 
        delet = delet[1:]
    else: 
        delet = [0, 0]
    
    m = max(delet) + min(delet)
    if str(m)[-1] == '8': 
        print(i, m)
        c += 1
        if c == 5: 
            break


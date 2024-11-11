for i in range(0, 10): 
    for j in range(0, 10): 
        r = int(f'12345{i}7{j}8')
        if r % 23 == 0: 
            print(r, r // 23)


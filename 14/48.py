althabet = '0123456789abcdefghijk'

for x in althabet: 
    y = 0
    s = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
    if s % 18 == 0: 
        c = 0
        for y in althabet: 
            s2 = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
            if s2 % 18 != 0: 
                break
            c += 1
        if c == 21: 
            print(x)
            y = 5
            print((int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) / 18)
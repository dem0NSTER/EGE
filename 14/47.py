althabet = '0123456789abcde'
althabet1 = '0123456789abcdefg'

for x in althabet: 
    for y in althabet1: 
        s = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if s % 131 == 0: 
            print(s / 131, x, y)


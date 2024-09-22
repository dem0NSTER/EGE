althabet = '0123456789abcde'

for x in althabet: 
    if (int(f'123{x}5', 15) + int(f'1{x}233', 15)) % 14 == 0: 
        print((int(f'123{x}5', 15) + int(f'1{x}233', 15)) / 14)
        break
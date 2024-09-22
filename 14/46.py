althabet  = '0123456789abcdefg'

for i in althabet: 
    if (int(f'9759{i}', 17) + int(f'3{i}108', 17)) % 11 == 0: 
        print((int(f'9759{i}', 17) + int(f'3{i}108', 17)) / 11)
        break
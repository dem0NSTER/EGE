althabet = '1 2 3 4 5 6 7 8 9 a c d e'.split()

for x in althabet: 
    # print(int(f'123{x}5', 15) + int(f'1{x}233'))
    if (int(f'123{x}5', 15) + int(f'1{x}233', 15)) % 14 == 0: 
        print((int(f'123{x}5', 15) + int(f'1{x}233', 15)) / 14)
        break
althabet = '1 2 3 4 5 6 7 8 9 a b c d e'.split()
althabet.reverse()

for x in althabet: 
    if (int(f'97968{x}21', 15) + int(f'7{x}23', 15)) % 14 == 0: 
        d = (int(f'97968{x}21', 15) + int(f'7{x}23', 15)) / 14
        break

assert d == 116047226
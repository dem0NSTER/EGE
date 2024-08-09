althabet = '1 2 3 4 5 6 7 8 9 a b c d e'.split()
althabet.reverse()

for x in althabet: 
    if (int(f'{x}3483491', 15) + int(f'4893{x}', 15)) % 14 == 0:
        print((int(f'{x}3483491', 15) + int(f'4893{x}', 15)) / 14)
        break
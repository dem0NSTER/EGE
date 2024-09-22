althabet1 = '0123456789a'
althabet2 = '0123456789ab'
althabet3 = '0123456789abcd'

for i in althabet1: 
    if int(f'3364{i}', 11) + int(f'{i}7946', 12) == int(f'55{i}87', 14): 
        print(int(f'55{i}87', 14))
        break
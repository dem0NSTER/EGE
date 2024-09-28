s = '0123456789abcde'



for i in s: 
    if (int(f'{i}3483491', 15) + int(f'4893{i}', 15)) % 14 == 0: 
        print((int(f'{i}3483491', 15) + int(f'4893{i}', 15)) // 14)
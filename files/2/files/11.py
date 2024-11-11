from math import ceil

for x in range(100, 0, -1): 
    one = ceil((24 * 7) / 8) + 4 + x
    all = one * 2048
    if all <= (70 * 2 ** 10): 
        print(x)
        break
from math import ceil

for i in range(1, 100): 
    num = ceil((261 * i) / 8)
    if num * 252500 > 31 * (2 ** 20): 
        print(2 ** i)
        break
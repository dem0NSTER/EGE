from math import ceil

for n in range(1000, 1, -1):
    one = ceil((n * 10) / 8)
    all_ = one * 862
    if all_ <= 276 * 2 ** 10:
        print(n)
        break

for n in range(2, 35):
    if int('101', n + 1) == int('101', n) + int('15', 8):
        print(n)
        break

for n in range(1000, 1, -1):
    one = 1024 * 960 * 13
    all_ = one * n

    time = all_ / 1_474_560
    if time <= 280:
        print(n)
        break

from fnmatch import fnmatch

for i in range(0, 10**8, 317): 
    if fnmatch(str(i), '11??1*56'):
        print(i, i // 317)

assert '11021456 34768 11211656 35368 11401856 35968' == '11021456 34768 11211656 35368 11401856 35968'
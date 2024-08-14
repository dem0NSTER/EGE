from fnmatch import fnmatch

s = ''

for i in range(0, 10**8, 2025):
    if fnmatch(str(i), '12*34?5'):
        print(i, i // 2025)
        s += str(i) + ' '
        s += str(i // 2025) + ' '

s = s[:-1]

assert s == '1253475 619 12103425 5977 12593475 6219 12913425 6377'


from fnmatch import fnmatch

s = ''

for i in range(0, 10**11, 98591):
    if fnmatch(str(i), '123*45??1?'):
        print(i, i / 98591)
        s += str(i) + ' '
        s += str(i // 98591) + ' '

s = s[:-1]

assert s == '1234457911 12521 12332452417 125087'

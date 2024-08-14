import fnmatch as fn

s = ''

for i in range(0, 10**8, 3123):
    if fn.fnmatch(str(i), '3?1*57'):
        print(i, i / 3123)
        s += str(i) + ' '
        s += str(i // 3123) + ' '

s = s[:-1]
assert s == '3619557 1159 30165057 9659 31101957 9959 35161857 11259'

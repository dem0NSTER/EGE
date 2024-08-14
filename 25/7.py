from fnmatch import fnmatch

for i in range(0, 10**9, 31): 
    if fnmatch(str(i), '12345?7?8'): 
        print(i, i / 31)

assert '123452788 3982348 123453718 3982378 123457748 3982508' == '123452788 3982348 123453718 3982378 123457748 3982508'

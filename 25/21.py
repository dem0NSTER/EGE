from fnmatch import fnmatch

for i in range(19, 10**9, 19): 
    if fnmatch(str(i), '1234?57?8'): 
        print(i, i // 19)

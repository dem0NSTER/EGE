from fnmatch import fnmatch
for i in range(0, 10**8, 6072): 
    if fnmatch(str(i), '5*4?48'): 
        print(i, i / 6072)
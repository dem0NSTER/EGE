from fnmatch import fnmatch

for i in range(0, 10**8, 2622): 
    if fnmatch(str(i), '1?4*6?8'): 
        print(i, i // 2622)


a = '''
154698 59
11468628 4374
12425658 4739
15401628 5874
16476648 6284
17433678 6649
19452618 7419
'''
b= '''
154698 59
11468628 4374
12425658 4739
15401628 5874
16476648 6284
17433678 6649
19452618 7419
'''

assert a == b
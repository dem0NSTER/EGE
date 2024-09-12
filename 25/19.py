from fnmatch import fnmatch

for i in range(0, 10**9, 3127): 
    if fnmatch(str(i), '12*93?1?'):
        print(i, i // 3127)

a = """
120993011
122093715
126193212
127293916
"""
b = '''
120993011
122093715
126193212
127293916
'''

assert a == b
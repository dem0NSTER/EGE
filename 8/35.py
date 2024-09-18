from itertools import product

c = 0

for i in product('0123456789', repeat=3): 
    code = ''.join(i)
    code_2 = ''.join(sorted(i))
    if code[0] == '0': 
        continue
    if code_2 == code: 
        print(code)
        c += 1
print(c)
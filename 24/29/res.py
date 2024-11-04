from itertools import product

s = open('24/29/1.txt').readline().lower()
# s = 'abczyzxaazxzyafezxzy'

stop = ''
for i in product('abcdef', repeat=3): 
    word = ''.join(i)
    stop += word

left = 0
max_len = 0
count = 0

for right in range(2, len(s)): 
    if s[right - 2] + s[right - 1] + s[right] in stop: 
        count += 1
    
    while count > 0: 
        if s[left] + s[left + 1] + s[left + 2] in stop: 
            count -= 1
        left += 1
    
    if count == 0: 
        max_len = max(max_len, right - left + 1)
    
print(max_len)

s = open('24/20/1.txt').readline().lower()

count_ab = 0
max_len = 0
left = 0

for right in range(1, len(s)): 
    if s[right - 1] + s[right] == 'ab': 
        count_ab += 1
    
    while count_ab > 50: 
        if s[left] + s[left + 1] == 'ab': 
            count_ab -= 1
        left += 1
    
    if count_ab == 50: 
        max_len = max(max_len, right - left + 1)
    
print(max_len)
    
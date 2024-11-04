s = open('24/21/1.txt').readline().lower()

left = 0
count_ro = 0
count_ror = 0
count_oro = 0
max_len = 0 

for right in range(1, len(s)): 
    if s[right - 1] + s[right] == 'ro': 
        count_ro += 1
    if right >= 2 and s[right - 2] + s[right - 1] + s[right] == 'ror': 
        count_ror += 1
    if right >= 2 and s[right - 2] + s[right - 1] + s[right] == 'oro': 
        count_oro += 1
    
    while count_oro > 0: 
        if s[left] + s[left + 1] + s[left + 2] == 'oro': 
            count_oro -= 1
        if s[left] + s[left + 1] == 'ro': 
            count_ro -= 1
        left += 1
    
    while count_ror > 0: 
        if s[left] + s[left + 1] + s[left + 2] == 'ror': 
            count_ror -= 1
        if s[left] + s[left + 1] == 'ro': 
            count_ro -= 1
        left += 1
    
    while count_ro > 21: 
        if s[left] + s[left + 1] == 'ro': 
            count_ro -= 1
        left += 1

    if count_ror == 0 and count_oro == 0 and count_ro == 21: 
        max_len = max(max_len, right - left + 1)

print(max_len)

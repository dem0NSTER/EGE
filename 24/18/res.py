s = open('24/18/1.txt').readline().lower()

left = 0
count_d = 0
max_len = 0

for right in range(len(s)): 
    if s[right] == 'd': 
        count_d += 1
    
    while count_d > 2: 
        if s[left] == 'd': 
            count_d -= 1
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)

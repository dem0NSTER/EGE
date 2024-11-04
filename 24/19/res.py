s = open('24/19/1.txt').readline().lower()

left = 0
count_t = 0
max_len = 0

for right in range(len(s)): 
    if s[right] == 't': 
        count_t += 1
    
    while count_t > 100: 
        if s[left] == 't': 
            count_t -= 1
        left += 1

    if count_t == 100: 
        max_len = max(max_len, right - left + 1)

print(max_len)

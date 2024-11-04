s = open('24/24/1.txt').readline().lower()

count = 0
left = 0
min_len = 10 ** 18 

for right in range(2, len(s)): 
    if s[right - 2] + s[right - 1] + s[right] == 'fat': 
        count += 1
    if s[right - 2] + s[right - 1] + s[right] == 'bad': 
        count += 1
    
    if count == 3: 
        while True: 
            if s[left + 1] + s[left + 2] + s[left + 3] == 'fat': 
                left += 1
                break
            if s[left + 1] + s[left + 2] + s[left + 3] == 'bad': 
                left += 1
                break
            left += 1
        
        if count == 3: 
            min_len = min(min_len, right - left + 1)
        count -= 1

print(min_len)
        
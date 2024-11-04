s = open('24/22/1.txt').readline().lower()

left = 0
min_len = 10 ** 18
count_dot = 0

for right in range(len(s)): 
    if s[right] == '.': 
        count_dot += 1
    
    # while count_dot == 7: 
    #     if s[left] == '.': 
    #         count_dot -= 1
    #     left += 1
    if count_dot == 7: 
        while True: 
            if s[left + 1] == '.': 
                left += 1
                break
            left += 1

        min_len = min(min_len, right - left + 1)
        count_dot -= 1

print(min_len)

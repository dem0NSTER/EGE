s = open('24/23/1.txt').readline().lower()

left = 0 
count_y = 0
count_x = 0
min_len = 10 ** 18

for right in range(len(s)): 
    if s[right] == 'x':
        count_x += 1
    if s[right] == 'y': 
        count_y += 1

    while count_y > 0: 
        if s[left] == 'y': 
            count_y -= 1
        if s[left] == 'x': 
            count_x -= 1
        left += 1
    
    if count_x >= 500: 
        while True: 
            if s[left + 1] == 'x': 
                left += 1
                break
            left += 1

        if count_x >= 500 and count_y == 0: 
            min_len = min(min_len, right - left + 1)
        count_x -= 1

print(min_len)

s = open('24.txt').readline().lower()


left = 0
m = 0
count_cd = 0

for right in range(1, len(s)):
    if s[right -1] + s[right] == 'cd':
        count_cd += 1

    while count_cd > 160:
        if s[left] + s[left + 1] == 'cd':
            count_cd -= 1
        left += 1

    if count_cd == 160:
        m = max(right - left + 1, m)

print(m)
        
    

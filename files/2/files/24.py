s = open('files/2/files/24_8378.txt').readline()

s = s.replace('ATGTTT', '*')
s = s.replace('ACATAA', '_')


c = 0
string = ''
for i in range(len(s)): 
    if s[i] == '*' and c == 0: 
        string += 'ATGTTT'
        c = 1

    elif c == 1 and s[i] == '_': 
        string += 'ACATAA'
        c = 0
        break
    
    elif c == 1: 
        string += s[i]
    
    
print(string)
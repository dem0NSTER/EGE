s = open('24/10/1.txt').readline().lower()
s = s.replace('n', '*').replace('o', '*').replace('p', '*')
s = s.replace('**', '* *').replace('**', '* *')
s = s.split()
print(len(max(s, key=len)))

"""*******************************************"""
s = open('24/10/1.txt').readline().lower()
s = s.replace('n', '*').replace('o', '*').replace('p', '*')
m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] + s[i] != '**': 
        m[i] = m[i - 1] + 1

print(max(m))

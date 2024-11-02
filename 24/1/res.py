s = open('24/1/1.txt').readline()
s = s.replace('C', ' ').replace('D', ' ')
s = s.split()
print(len(max(s, key=len)))
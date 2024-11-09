import string

s = open('24/44/1.txt').readline()

res = {x: s.count(x) for x in string.ascii_uppercase}

print(max(res.values()) - min(res.values()))

s = open('24/43/1.txt').readline().lower()

res = {x: s.count(x) for x in 'abcdefghijklmnopqrstuvwxyz'}

max_len = max(res.values())

for i in 'abcdefghijklmnopqrstuvwxyz': 
    if res[i] == max_len: 
        print(i, res.get(i), sep='')
        break

print(res)

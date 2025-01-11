n = 1000
s = 600
f = open('26/3/1.txt')

data = [int(x) for x in f]
data.sort(reverse=True)

count = 0
while len(data) > 0: 
    reis = []
    try: 
        while sum(reis) + min(data) <= s: 
            for i in range(len(data)): 
                if sum(reis) + data[i] <= s: 
                    reis += [data.pop(i)]
                    break
    except: 
        ...
    count += 1
    

print(count, sum(reis))

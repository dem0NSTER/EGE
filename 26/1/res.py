file = open('26/1/1.txt')
s = 100000
n = 1000

data = [int(i) for i in file]

data.sort()
arhive = []

while sum(arhive) + data[0] <= s: 
    for i in range(len(data) - 1, 0, -1):
        if sum(arhive) + data[i] <= s: 
            arhive += [data.pop(i)]
            break

    if sum(arhive) + data[0] <= s: 
        arhive += [data.pop(0)]
    
print(len(arhive), arhive[-1])

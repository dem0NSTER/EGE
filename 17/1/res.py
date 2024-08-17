with open('17_Demo22.txt') as file: 
    s = file.read()

s1 = [int(i) for i in s]

res = []

for i in range(len(s) - 1): 
    print(s1[i], s1[i + 1])
    
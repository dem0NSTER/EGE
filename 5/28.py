res = []

for n in range(1, 1000): 
    n2 = bin(n)[2:]
    summ = sum(int(i) for i in n2)
    num = n2 + str(summ % 2)
    summ = sum(int(i) for i in num)
    num2 = num + str(summ % 2)

    if int(num2, 2) > 80:
        res.append(int(num2, 2))

print(min(res))
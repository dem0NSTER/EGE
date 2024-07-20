"""Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма
всех выбранных чисел не делилась на 3 и при этом была минимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно
число — минимально возможную сумму, соответствующую условиям задачи.
№ 27889
"""

summ = 0
nums = []
difference = 10000

with open('27-B_demo.txt') as file:
    data = file.read().split('\n')

for i in data[1::]:
    a = [int(x) for x in i.split()]
    if len(a) == 2:
        nums.append(a)

for num in nums:
    summ += min(num)
    if (max(num) - min(num)) % 3 != 0:
        difference = max(difference, (max(num) - min(num)))

if summ % 3 != 0:
    print(summ)
else:
    print(summ - difference)
# 67088, 200157478

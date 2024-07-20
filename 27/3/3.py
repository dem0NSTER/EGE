"""
Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма
всех выбранных чисел не делилась на 5 и при этом была максимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно
число— максимально возможную сумму, соответствующую условиям задачи.
№27890
"""
summ = 0
data = []
difference = 10000

with open('27-B_1.txt') as file:
    all = file.read().split('\n')


for i in all[1::]:
    nums = [int(num) for num in i.split()]
    if len(nums) == 2:
        data.append(nums)
    else:
        print(f'nums: {nums}')

for nums in data:
    summ += max(nums)
    if (max(nums) - min(nums)) % 5 != 0:
        difference = min(difference, (max(nums) - min(nums)))

if summ % 5 != 0:
    print(summ)
else:
    print(summ - difference)
# 118951, 394491666

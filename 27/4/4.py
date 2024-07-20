"""
Последовательность натуральных чисел характеризуется числом Х— наибольшим числом,
кратным 14 и являющимся произведением двух элементов последовательности с различными
номерами. Гарантируется, что хотя бы одно такое произведение в последовательности есть.
№ 27891
"""

with open('27-B_2.txt') as f:
    data = f.read().split('\n')

max_14 = 0
max_7 = 0
max_2 = 0
int_data = [int(x) for x in data[1::]]


max_count = max(int_data)
for i in int_data:
    if i % 14 == 0 and i > max_14:
        max_14 = i

for i in int_data:
    if i % 7 == 0 and i > max_7:
        max_7 = i


for i in int_data:
    if i % 2 == 0 and i > max_14:
        max_2 = i

if max_14 * max_count > max_2 * max_7:
    print(max_14 * max_count)
else:
    print(max_2 * max_7)
# 447552, 994000
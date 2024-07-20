"""
На вход программы поступает последовательность из N натуральных чисел.
Рассматриваются все пары различных элементов последовательности, у которых
различные остатки от деления на d=160 и хотя бы одно из чисел делится на p=7.
Среди таких пар, необходимо найти и вывести пару с максимальной суммой элементов.
№ 28129
"""

with open('28129_Az.txt') as f:
    data = f.read().split('\n')

data = [int(x) for x in data[1::]]

def7 = {}
def160 = {}

for i in data:
    if i % 7 == 0:
        def7[i] = i % 160

for i in data:
    def160[i] = i % 160


while True:
    if def160[max(def160.keys())] != def7[max(def7.keys())]:
        a = [int(max(def160)), int(max(def7))]
        a.sort()
        print(a)
        break
    else:
        if max(def160) > max(def7):
            del def7[max(def7)]
        else:
            del def160[max(def160)]
# 728, 977 \\ 9982, 9992
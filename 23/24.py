"""
Исполнитель Быбыл преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:

1. Прибавь 3
2. Умножь на 3

Сколько различных чётных чисел, меньших 25, может получить Быбыл из исходного числа 3?
"""
def f(n: int, finish: int): 
    if n == finish: 
        return 1
    if n > finish: 
        return 0
    if n < finish: return f(n + 3, finish) + f(n * 3, finish)

c = 0
for finish in range(4, 25, 2): 
    if f(3, finish) != 0: 
        c += 1
    
print(c)
num = int(input())
base = 0
while not (2 <= base <= 9):
    base = int(input('Основание (2-9): '))

new = ''

while num > 0:
    remainder = num % base
    new += str(remainder) 
    num = num // base

print(new[::-1])
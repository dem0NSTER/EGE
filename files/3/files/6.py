from turtle import *

speed(1000)
left(90)
k = 30
screensize(2000, 2000) 
down()

for _ in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)

up()
forward(1 * k)
right(90)
forward(5 * k)
left(90)

down()
for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)

up()

for x in range(100):
    for y in range(100):
        goto(x * k, y * k)
        dot(4, 'red')
        
done()

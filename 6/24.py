from turtle import * 


tracer(0)
screensize(2000, 2000)
k = 30
left(90)
down()

for _ in range(4): 
    forward(9 * k)
    left(270)

up()
for _ in range(3): 
    forward(1 * k)
    left(270)
    forward(1 * k)
    left(90)

down()

for _ in range(2): 
    forward(9 * k)
    left(270)
    forward(11 * k)
    left(270)

up()

for x in range(-5, 20): 
    for y in range(-5, 15): 
        goto(x * k, y * k)
        dot(4, 'red')

done()

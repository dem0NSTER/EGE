from turtle import * 

tracer(0)
down()
k = 50
screensize(20000, 20000)


def move(x, y): 
    position = pos()
    goto(position + (x, y))


for i in range(15):
    move(10*k, 10*k)
    move(3*k, -6*k)
    move(-9*k, 3*k)

up()

for x in range(-50, 50): 
    for y in range(-50, 50): 
        setpos(x * k, y * k)
        dot(4, 'red')

done()
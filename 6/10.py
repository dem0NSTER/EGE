from turtle import * 

tracer(0)
down()
right(90)
k = 50
screensize(2000, 2000)

for i in range(8): 
    for i in range(4):
        forward(5 * k)
        right(30)
        forward(6 * k)
        right(150)
    right(60)

up()

for x in range(-50, 50): 
    for y in range(-50, 50): 
        setpos(x * k, y * k)
        dot(4, 'red')

done()
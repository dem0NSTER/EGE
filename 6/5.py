from turtle import * 

k = 30
tracer(0)
pendown()
left(90)

for i in range(11): 
    forward(4 * k)
    right(60)

penup()

canvas = getcanvas()
c = 0

for x in range(-20, 20): 
    for y in range(-20, 20): 
        setpos(x * k, y * k)
        dot(3, 'red')

done()
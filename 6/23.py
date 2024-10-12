from turtle import * 

tracer(0)
left(90)
down()
k = 50
for _ in range(6): 
    forward(4 * k)
    right(60)

up()
for x in range(-10, 10): 
    for y in range(-10, 10): 
        goto(x * k, y * k)
        dot(4, 'red')

done()
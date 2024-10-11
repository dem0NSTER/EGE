from turtle import * 

tracer(0)
left(90)
pendown()
k = 35

for i in range(9): 
    forward(3 * k)
    right(40)

up()

for x in range(-10, 10): 
    for y in range(-10, 10): 
        setpos(x * k, y * k)
        dot(3, 'red')

done()
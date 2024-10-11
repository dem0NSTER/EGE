from turtle import * 

tracer(0)
right(90)
down()
k = 50
screensize(2000, 2000)

for i in range(2): 
    forward(7 * k) 
    right(30)
    forward(8 * k)
    right(150)

up()
for x in range(-20, 20): 
    for y in range(-20, 20): 
        setpos(x * k, y * k)
        dot(4, 'red')

done()
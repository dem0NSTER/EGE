from turtle import * 

tracer(0)
screensize(2000, 2000)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


down()
k = 40

for _ in range(2): 
    move(6 * k, 2 * k)
    move(0 * k, -2 * k)

for _ in range(3): 
    move(2 * k, -1 * k)
    move(-2 * k, -1 * k)

for _ in range(6): 
    move(-2 * k, 1 * k)

up()
for x in range(-30, 30): 
    for y in range(-30, 30): 
        setpos(x * k, y * k)
        dot(4, 'red')

done()

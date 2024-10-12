from turtle import * 

tracer(0)
screensize(2000, 2000)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


down()
k = 40
for _ in range(5): 
    move(5 * k, 4 * k)
    move(4 * k, -4 * k)
    move(-7 * k, -2 * k)
    move(-2 * k, 2 * k)


up()
for x in range(-100, 100): 
    for y in range(-100, 100): 
        setpos(x * k, y * k)
        dot(4, 'red')

done()

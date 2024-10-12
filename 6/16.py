from turtle import * 

tracer(0)
screensize(2000, 2000)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


k = 40
down()
for _ in range(1): 
    move(6 * k, 8 * k)
    move(-8 * k, 4 * k)
    move(2 * k, -12 * k)
    
up()
for x in range(-100, 100): 
    for y in range(-100, 100): 
        setpos(x * k, y * k)
        dot(4, 'red')
    
done()

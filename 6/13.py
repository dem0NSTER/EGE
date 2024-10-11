from turtle import * 

speed(1000)

def move(x, y): 
    p = pos()
    setpos(p + (x, y))

down()
k = 100

for i in range(10): 
    move(4 * k, 3 * k)
    move(-4 * k, 10 * k)
    move(18 * k, -12 * k)
    move(-24 * k, - 12 * k)

up()
canvas = getcanvas()
c = 0

for x in range(-1000, 1000): 
    for y in range(-1000, 1000): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point != (): 
            c+= 1
print(c)
done()
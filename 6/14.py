from turtle import * 

speed(1000)
def move(x, y): 
    p = pos()
    setpos(p + (x, y))

down()
k = 1000

for i in range(7): 
    move(6 * k, -9 * k)
    move(-6 * k, 2 * k)
    move(12 * k, 3 * k)

up()
canvas = getcanvas()
c = 0

for x in range(-1000, 1000): 
    for y in range(-1000, 1000): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point != (): 
            c += 1

print(c)
from turtle import * 

speed(10000)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


down()
k = 10
begin_fill()
for _ in range(3): 
    move(90 * k, 90 * k)
    move(-60 * k, 0)
    move(-30 * k, -90 * k)
end_fill()

up()
canvas = getcanvas()
c = 0
for x in range(-300, 300): 
    for y in range(-300, 300): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)

done()

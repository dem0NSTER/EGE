from turtle import * 

speed(1000)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


down()
k = 100
begin_fill()
for _ in range(1): 
    move(5 * k, 15 * k)
    move(111 * k, 0 * k)
    move(-60 * k, -15 * k)
    move(-56 * k, 0 * k)
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
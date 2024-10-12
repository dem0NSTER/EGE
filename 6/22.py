from turtle import * 

tracer(0)
left(90)
down()
k = 1000
begin_fill()
for _ in range(3): 
    forward(30 * k)
    left(120)
end_fill()

up()
canvas = getcanvas()
c = 0
for x in range(-50, 50): 
    for y in range(-50, 50): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)
done()
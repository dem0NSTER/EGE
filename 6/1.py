from turtle import * 
k = 30

tracer(0)

pendown()
begin_fill()
for i in range(6): 
    forward(3 * k)
    left(60)

end_fill()
penup()

c = 0

canvas = getcanvas()
for x in range(-100, 100): 
    for y in range(-100, 100): 
        point = canvas.find_overlapping(x*k, y*k, x*k, y*k)
        if point == (5, ): 
            c += 1

print(c)
done()
from turtle import * 

k = 1000

tracer(0)

left(90)
pendown()
begin_fill()

right(90)
for i in range(3): 
    right(45)
    forward(12 * k)
    right(45)
right(315)
forward(12 * k)
for i in range(2): 
    right(90)
    forward(12 * k)
end_fill()

penup()
canvas = getcanvas()
c = 0

for x in range(-300, 300): 
    for y in range(-300, 300): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)
done()
from turtle import * 

k = 200

tracer(0)
left(90)
pendown()
begin_fill()
for i in range(3): 
    forward(123 * k)
    right(120)
end_fill()

canvas = getcanvas()
c = 0

for x in range(-300, 300): 
    for y in range(-300, 300): 
        point = canvas.find_overlapping(x* k, y* k, x* k, y* k)
        if point == (5, ): 
            c += 1

print(c)
done()

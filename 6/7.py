from turtle import * 

speed(1000)
right(90)
k = 100
down()

begin_fill()
for i in range(12): 
    for i in range(3): 
        forward(3 * k)
        right(90)
    left(180)
end_fill()
up()
canvas = getcanvas()
c = 0

for x in range(-500, 500): 
    for y in range(-500, 500): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)
done()
from turtle import * 

speed(1000)
left(90)
down()
k = 100
screensize(2000, 2000)

begin_fill()
right(45)
for _ in range(4): 
    forward(55 * k)
    right(90)
end_fill()

up()
canvas = getcanvas()
c = 0
for x in range(-100, 100): 
    for y in range(-100, 100): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)
done()
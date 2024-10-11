from turtle import * 

speed(1000)
right(90)
down()
k = 50
screensize(2000, 2000)

begin_fill()
forward(9 * k)
right(90)
for i in range(2): 
    forward(3 * k)
    right(90)
    forward(3 * k)
    right(270)
for i in range(2): 
    forward(3 * k)
    right(90)
forward(9 * k)
end_fill()

up()
canvas = getcanvas()
c = 0

for x in range(-20, 20): 
    for y in range(-20, 20): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point != (): 
            c += 1

print(c)
done() # 73
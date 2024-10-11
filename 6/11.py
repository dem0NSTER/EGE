from turtle import * 

tracer(0)
down()
k = 200

begin_fill()
for i in range(1): 
    setpos(3 * k, 6 * k)
    setpos(10 * k, 4 * k)
    setpos(0 * k, 0 * k)
end_fill()

up()
canvas = getcanvas()
c = 0

for x in range(-20, 20): 
    for y in range(-20, 20): 
        point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if point == (5, ): 
            c += 1

print(c)
done() # 22
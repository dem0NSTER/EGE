from turtle import * 

# speed(100)
tracer(0)
screensize(2000, 2000)
left(90)
down()
k = 50
# begin_fill()
for _ in range(3): 
    left(90)
    for _ in range(4): 
        forward(4 * k)
        right(90)
# end_fill()
up()

# c = 0
# canvas = getcanvas()
# for x in range(-100, 100): 
#     for y in range(-100, 100): 
#         dot = canvas.find_overlapping(x * k, y * k, x * k, y *k)
#         if dot == (5, ): 
#             c += 1

# print(c)
# done()

for x in range(-20, 20): 
    for y in range(-20, 20): 
        goto(x * k, y * k)
        dot(4, 'red')

done()
    
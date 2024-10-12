from turtle import * 

tracer(0)


def move(x, y): 
    p = pos()
    goto(p + (x, y))


down()
k = 40
screensize(2000, 2000)

for _ in range(3): 
    move(-3 * k, -4 * k)
    move(-12 * k, -5 * k)
    move(15 * k, 8 * k)
    move(0 * k, 1 * k)

up()
canvas = getcanvas()
c = 0

# for x in range(-1000, 1000): 
#     for y in range(-1000, 1000): 
#         point = canvas.find_overlapping(x * k, y * k, x * k, y * k)
#         if point != (): 
#             c += 1
# print(c) # 4

for x in range(-100, 100): 
     for y in range(-100, 100):
         setpos(x * k, y * k)
         dot(4, 'red')
        
done()
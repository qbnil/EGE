from turtle import *
tracer(0)
left(90)
m = 10

for _ in range (2):
    forward(35*m)
    right(90)
    forward(10*m)
    right(90)

penup()
forward(2*m)
right(90)
forward(2*m)
left(90)
pendown()
for _ in range(2):
    forward(45*m)
    right(90)
    forward(20*m)
    right(90)

penup()
for x in range(-10, 30):
    for y in range(-15, 70):
        goto(x*m, y*m)
        dot(3)
Screen().exitonclick()

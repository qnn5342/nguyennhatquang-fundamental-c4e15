from turtle import *
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed (0)
for i in colors:
    color(i)
    begin_fill()
    for x in range(2):
        forward(50)
        left (90)
        forward(100)
        left (90)
    penup()
    forward (50)
    pendown()
    end_fill()
left(90)
forward(100)
right(90)

mainloop()

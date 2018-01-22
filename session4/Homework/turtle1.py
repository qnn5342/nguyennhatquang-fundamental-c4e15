from turtle import *
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

speed(0)

sides = 2
turn = 0
for u in colors:
    sides +=1
    turn +=1
    color(u)
    for i in range(sides):
        forward(100)
        left (360/sides)
    

mainloop()

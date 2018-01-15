from turtle import *
shape("turtle")
odd = "blue"
even = "red"
sides = 2
turn = 0
for u in range (4):
    sides +=1
    turn +=1
    if turn %2 ==0:
        color(even)
    else:
        color(odd)
    for i in range(sides):
        forward(100)
        left (360/sides)
    print (turn)

mainloop()

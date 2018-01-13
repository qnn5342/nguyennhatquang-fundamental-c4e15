from turtle import *
shape("turtle")
n = int(input("insert number of steps: "))
e = {"red", "white","blue"}
for i in e:
    color(i)
    forward(20)
mainloop()

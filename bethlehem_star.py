from turtle import *

t = Turtle()
t.color("red", "yellow")
t.begin_fill()
for i in range(8):
    t.right(180 - 180/4)
    t.fd(300)
t.end_fill()
done()

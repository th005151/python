import turtle
import time

t1=turtle.Turtle()
t1.screen.reset()
t1.shape("turtle")
n=50
for index in range(n):
    t1.forward(index*2)
    t1.left(20)


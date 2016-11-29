
from turtle import *

def square(edge):
    for step in range(4):
        forward(edge)
        left(90)
    forward(edge)

def go(length, n):
    if n == 0:
        square(length)
    else:
        go(length/3, n-1)

        penup()
        forward(length/3)
        pendown()

        go(length/3, n-1)

for i in range(0, 5):
    penup()
    goto(0, 0)
    pendown()
    go(250, i)

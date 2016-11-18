from turtle import *

def init():
    shape('turtle')
    shapesize(2)
    color('black', 'darkgreen')
    width(3)
    speed(10)
    penup()
    goto(-200, 0)
    

def spiral_1():
    """ перо поднято по окончании рисования
    """
    pendown()
    length = 10
    alpha = 30
    for i in range(30):
        forward(length)
        left(alpha)
        alpha *= 0.95
    penup()    

def spiral_2():
    """ перо поднято по окончании рисования
    """
    pendown()
    length = 10
    alpha = 10
    for i in range(100):
        forward(length)
        left(alpha)
        length *= 1.01
    penup()
    
init()
spiral_1()
init()
spiral_2()
    

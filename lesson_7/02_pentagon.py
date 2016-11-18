from turtle import *

def init():
    shape('turtle')
    shapesize(2)
    color('black', 'darkgreen')
    width(3)
    penup()
    backward(200)

def pentagon(edge_length):
    """ перо поднято по окончании
        рисования пятиугольника
        edge_length - длина ребра
    """
    pendown()
    begin_fill()
    for side in range(5):
        forward(edge_length)
        left(360/5)
    end_fill()
    penup()

def star(length):
    """ перо поднято по окончании
        рисования пятиугольника
        length - длина ребра
    """
    pendown()
    begin_fill()
    for side in range(5):
        forward(length)
        right(2*360/5)
    end_fill()
    penup()
        
init()
star(150)
forward(200)
pentagon(70)
hideturtle()

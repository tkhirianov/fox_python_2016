from turtle import *

def init():
    shape('turtle')
    shapesize(2)
    color('black', 'darkgreen')
    width(3)
    speed(10)
    penup()
    backward(300)

def polygon(edges_number, edge_length):
    """ перо поднято по окончании
        рисования многоугольника
        edges_number - количество рёбер (углов)
        edge_length - длина ребра
    """
    pendown()
    begin_fill()
    for side in range(edges_number):
        forward(edge_length)
        left(360/edges_number)
    end_fill()
    penup()

def star(rays_number, length):
    """ перо поднято по окончании рисования звезды
        length - длина ребра
        rays_number - количество лучей (нечётное!)      
    """
    pendown()
    begin_fill()
    for side in range(rays_number):
        forward(length)
        right((rays_number//2)*360/rays_number)
    end_fill()
    penup()    
        
init()
for n in range(3, 10):
    polygon(n, 50)
    forward(100)
    
backward(7*100)
right(90)
forward(150)
left(90)

for n in range(3, 16, 2):
    star(n, 80)
    forward(100)
    

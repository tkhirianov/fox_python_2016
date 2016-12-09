from turtle import *
from math import *

scale_factor = 30
current_x = 0
current_y = 0

def on_vector(x, y):
    """черепашка в начале повёрнута на "восток"
       и в конце тоже повёрнута на "восток"
    """
    global current_x, current_y
    
    alpha = calculate_angle(x, y)
    length = scale_factor*(x**2 + y**2)**0.5
    left(alpha)
    forward(length)
    right(alpha)
    current_x += x
    current_y += y
    
def to_point(x, y):
    on_vector(x - current_x, y - current_y)

def calculate_angle(x, y):
    if x == 0:
        if y == 0:
            return 0
        elif y > 0:
            return 90
        else:  # y < 0
            return -90
    elif x > 0:
        return degrees(atan(y/x))
    else:  # x < 0
        return 180 + degrees(atan(y/x))

def init_drawman():
    """ Инициализация Чертёжника """
    clear()
    penup()
    speed(1000)
    draw_coords_web()
    draw_axis()
    color('blue')

def draw_coords_web():
    """ После рисования сетки координат
        ставит Чертёжника в точку (0, 0)
        с поднятым пером
    """
    penup()
    color('lightgray')
    for x in range(-10, 11):
        to_point(x, -10)
        pendown()
        to_point(x, +10)
        penup()
    for y in range(-10, 11):
        to_point(-10, y)
        pendown()
        to_point(+10, y)
        penup()
    to_point(0, 0)
    
def draw_axis():
    """ После рисования сетки координат
        ставит Чертёжника в точку (0, 0)
        с поднятым пером
    """
    penup()
    color('black')
    width(3)
    to_point(-10, 0)
    pendown()
    to_point(+10, 0)
    penup()
    to_point(0, -10)
    pendown()
    to_point(0, +10)
    penup()
    to_point(0, 0)

def test_drawman():
    pendown()
    for i in range(10):
        on_vector(-1, 1)
        on_vector(0, -1)
    penup()
    to_point(0, 0)
    pendown()
    to_point(0, 2)
    to_point(2, 2)
    to_point(2, 0)
    to_point(0, 0)
    penup()

if __name__ == '__main__':
    init_drawman()
    test_drawman()

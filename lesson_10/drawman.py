from turtle import *
from math import *

scale_factor = 30

def on_vector(x, y):
    """черепашка в начале повёрнута на "восток"
       и в конце тоже повёрнута на "восток"
    """
    alpha = calculate_angle(x, y)
    length = scale_factor*(x**2 + y**2)**0.5
    left(alpha)
    forward(length)
    right(alpha)
    print(alpha, x, y)
    
def to_point(x, y):
    pass  #FIXME


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

def test_drawman():
    for i in range(10):
        on_vector(-1, 1)
        on_vector(0, -1)
    
    to_point(0, 0)
    to_point(0, 2)
    to_point(2, 2)
    to_point(2, 0)
    to_point(0, 0)

if __name__ == '__main__':
    test_drawman()

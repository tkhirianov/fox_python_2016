from turtle import *

def init_turtle():
    speed(100)
    penup()
    goto(-50, 0)
    pendown()


def my_forward(L, width):
    if L < 2:
        forward(L)
    else:
        pensize(width)
        forward(L/2)
        my_forward(L/2, width/2)


def snowy_forward(L, n):
    if n == 0:
        forward(L)
    else:
        snowy_forward(L/3, n-1)
        left(60)
        snowy_forward(L/3, n-1)
        right(120)
        snowy_forward(L/3, n-1)
        left(60)
        snowy_forward(L/3, n-1)


def koh_snow():
    snowy_forward(300, 2)
    right(120)
    snowy_forward(300, 3)
    right(120)
    snowy_forward(300, 4)
    right(120)

    
def levi_curve(L, n):
    if n == 0:
        forward(L)
    else:
        left(45)
        levi_curve(L/2**0.5, n-1)
        right(90)
        levi_curve(L/2**0.5, n-1)
        left(45)


def levi_demo():
    for i, col in enumerate(['red', 'green', 'blue', 'black']*5):
        init_turtle()
        color(col)
        levi_curve(100, i)

    
def dragon_curve(L, n, sign=+1):
    if n == 0:
        forward(L)
    else:
        left(45*sign)
        dragon_curve(L/2**0.5, n-1, +1)
        right(90*sign)
        dragon_curve(L/2**0.5, n-1, -1)
        left(45*sign)


if __name__ == "__main__":
    init_turtle()
    dragon_curve(200, 10)
    

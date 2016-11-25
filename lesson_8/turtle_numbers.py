from turtle import *

def paint_figure(lengths, degrees):
    """ Рисует произвольную фигуру, совершая N шагов
        length - список длин шагов
        degrees - список поворотов, совершаемых перед шагом
    """
    pendown()
    for i in range(len(degrees)):
        left(degrees[i])
        forward(lengths[i])
    penup()
    forward(a + a*0.3)

a = 50
c = a*2**0.5
one_degrees = [45, 0, -135, 0, 90]
one_lengths = [-c, c, 2*a, -2*a, 0]

two_degrees = []
two_lengths = []

three_degrees = [0, 0, 45, -45, 45, 0, -45, 45, -45]
three_lengths = [-a, a, -c, a, -c, c, -a, c, 0]

paint_figure(one_lengths, one_degrees)
paint_figure(two_lengths, two_degrees)
paint_figure(three_lengths, three_degrees)

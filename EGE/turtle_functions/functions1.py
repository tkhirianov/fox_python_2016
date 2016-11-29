
from turtle import *

def square(edge):
    """ документ-строка функции: описывает что делает функция,
        смысл и допустимые типы и значения параметров

        рисует квадрат
        заканчивается там же, где начинается (в той же точке)
        перо по окончании рисования поднято
        
    """
    pendown()
    for step in range(4):
        forward(edge)
        left(90)
    penup()

def polygone(edge, n, doing):
    pendown()
    for step in range(n):
        doing(edge)  # вызываем некую функцию, переданную как параметр
        forward(edge)
        right(360/n)
    penup()

speed(100)
penup()
for i in range(1, 7):
    l = 10
    polygone(l, i+2, square)
    forward(l*5)

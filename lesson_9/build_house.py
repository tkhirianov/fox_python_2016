from turtle import *
from math import *

def main():
    penup()
    build_house(100)
    forward(150)
    build_house(80)
    forward(120)
    build_house(60)

def build_house(house_size):
    """ рисует дом примерно квадратный
        размера house_size пикселов по горизонтали
        черепашка при вызове функции находится посередине низа стены
        по окончании черепашка будет находиться там же
        смотрит при этом направо, перо поднято
    """
    build_foundation(house_size*1.1)
    build_walls(house_size, house_size*0.7)
    build_roof(house_size)
    penup()
    right(90); forward(house_size*0.7); left(90)

def build_foundation(width):
    """ рисует основание дома ширины width
        черепашка при вызове функции находится
        посередине верхушки фундамента
        по окончании черепашка будет находиться там же
        смотрит при этом направо
    """
    pendown()
    color('brown', 'grey')
    begin_fill()
    forward(width//2)
    right(90)
    forward(width//6)
    right(90)
    forward(width)
    right(90)
    forward(width//6)
    right(90)
    forward(width//2)
    end_fill()
    penup()
    
def build_walls(width, height):
    """ рисует стены дома ширины width и высоты height
        черепашка при вызове функции находится посередине низа стены
        по окончании черепашка будет находиться посередине верха стены
        смотрит при этом направо
    """
    pendown()
    color('black', 'red')
    begin_fill()
    forward(width//2)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width//2)
    end_fill()
    penup()
    # поднимемся на середину верха стены:
    left(90); forward(height); right(90)
    
def build_roof(width):
    """ рисует крышу дома ширины width
        черепашка при вызове функции находится посередине низа крыши
        по окончании черепашка будет находиться там же
        смотрит при этом направо
    """
    pendown()
    color('darkblue', 'blue')
    begin_fill()
    forward(width//2)
    left(180-30)
    L = (width//2)/cos(radians(30))
    forward(L)
    left(2*30)
    forward(L)
    left(180-30)
    forward(width//2)
    end_fill()
    






if __name__ == '__main__':
    main()

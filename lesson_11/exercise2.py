from drawman import *


def main():
    init_drawman()
    A = [(0, 0), (1, 1), (3, 0), (6, 2), (7, 0)]
    draw_curve(A)
    color('green', 'yellow')
    fill_polygon(A)
    B = [(x, -y) for x, y in A]
    fill_polygon(B)


def draw_curve(A):
    penup()
    to_point(*A[0])
    pendown()
    for x, y in A:  # NB! Пробегаем кортежем переменных по списку кортежей!
        to_point(x, y)
    penup()

def fill_polygon(A):
    begin_fill()
    draw_curve(A)
    pendown()
    to_point(*A[0])
    penup()
    end_fill()
    

main()

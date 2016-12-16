from drawman import *


def main():
    init_drawman()
    A = [(1, 1), (3, 0), (6, 2), (8, -5)]
    draw_curve(A)



def draw_curve(A):
    penup()
    to_point(A[0][0], A[0][1])
    pendown()
    for point in A:
        x, y = point
        to_point(x, y)
    penup()

def fill_polygon(A):
    begin_fill()
    draw_curve(A)
    to_point(A[0][0], A[0][1])
    end_fill()

main()

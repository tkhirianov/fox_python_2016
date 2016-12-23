from drawman import *
from math import *

def two_point_lists(A, B):
    for x1, y1 in A:
        for x2, y2 in B:
            penup()
            to_point(x1, y1)
            pendown()
            to_point(x2, y2)

def generate_circle_point_list(R, N):
    """ генерирует и возвращает список из N точек, лежащих на окружности
        радиуса R """
    A = []
    for i in range(N):
        alpha = radians(i*360/N)
        x = R*cos(alpha)
        y = R*sin(alpha)
        A.append((x, y))
    return A

def main():
    init_drawman()
    
    color('blue')
    width(1)
    C = generate_circle_point_list(8, 30)
    two_point_lists(C, C)
    
    #color('red')
    #A = [(7, 5), (3, 5), (5, 5)]
    #B = [(6, 1), (4, 1)]
    #two_point_lists(A, B)

main()

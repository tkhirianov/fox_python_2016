from drawman import *
from math import *

def draw_curve(A):
    penup()
    to_point(*A[0])
    pendown()
    for x, y in A:  # NB! Пробегаем кортежем переменных по списку кортежей!
        to_point(x, y)
    penup()

def draw_graph(f, graph_color='blue', a=-10, b=10, N=100):
    d = (b-a)/(N-1)
    graph = [(a+i*d, f(a+i*d)) for i in range(N)]
    color(graph_color)
    draw_curve(graph)

def f1(x):
    return 0.01*x**5 + 0.02*x**4 - 0.2*x**3 - 0.2*x**2 - x - 2

def f2(x):
    return 1/x

def bisection(f, a, b, epsilon=0.00000001):
    assert(f(a)*f(b) < 0, 'Простите, функция имеет одинаковый знак в точках a и b')
    while b - a > 2*epsilon:
        c = (a + b)/2
        if f(c) == 0:
            return c  # угадали корень
        elif f(c)*f(a) < 0:
            a, b = a, c
        else:
            a, b, = c, b
    return (a+b)/2

def main():
    init_drawman()
    draw_graph(f1, 'magenta')
    draw_graph(f2, 'cyan')
    draw_graph(sin, 'green')
    draw_graph(cos, 'blue')
    draw_graph(exp, 'red')
    print('положительный корень функции f1:', bisection(f1, 0, 10))

main()

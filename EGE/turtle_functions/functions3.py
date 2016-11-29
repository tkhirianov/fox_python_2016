
from turtle import *

def go_snowy(length, n):
    if n == 0:
        forward(length)
    else:
        go_snowy(length/3, n-1)
        left(60)
        go_snowy(length/3, n-1)
        right(120)
        go_snowy(length/3, n-1)
        left(60)
        go_snowy(length/3, n-1)

speed(100)
for i in range(3):
    go_snowy(250, 5)
    right(120)

from drawman import *

colours = ['red', 'green', 'blue']*5
back_colours = ['pink', 'lightgreen', 'lightblue']*5

init_drawman()
for i in range(10, 0, -1):
    pendown()
    color(colours[i], back_colours[i])
    begin_fill()
    on_vector(i, 0)
    on_vector(0, i)
    on_vector(-i, 0)
    on_vector(0, -i)
    end_fill()
    penup()

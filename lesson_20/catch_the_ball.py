from tkinter import *
from random import *

screen_width = 600
screen_height = 400
r_min = 10
r_max = 30
dt = 10  # микросекунд


class MainWindow:
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(root)
        self.canvas["width"] = screen_width
        self.canvas["height"] = screen_height
        self.canvas.pack()

        self.ball = None
        self.scores = 0
        self.init_game()
        self.game_cycle()  # запуск игрового цикла

        self.canvas.bind("<Button-1>", self.mouse_click)
        self.root.mainloop()

    def init_game(self):
        x = randint(0, screen_width-1)
        y = randint(0, screen_height-1)
        r = randint(r_min, r_max)
        self.ball = Ball(x, y, r)

    def game_cycle(self, *ignore):
        self.canvas.after(dt, self.game_cycle)  # перезапуск цикла
        # FIXME: что-то делаем с шариком

class Ball:
    def __init__(self, x, y, r):
        pass  #FIXME!

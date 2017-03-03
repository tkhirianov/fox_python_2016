from tkinter import *
from random import *

screen_width = 600
screen_height = 400
r_min = 10
r_max = 30
dt = 10  # микросекунд
ball_sprite_filename = "ball_sprite.png"


class MainWindow:
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()

        self.ball = None
        self.scores = 0
        self.init_game()
        self.game_cycle()  # запуск игрового цикла

        canvas.bind("<Button-1>", self.mouse_click)

    def init_game(self):
        x = randint(0, screen_width-1)
        y = randint(0, screen_height-1)
        r = randint(r_min, r_max)
        self.ball = Ball(x, y, r)

    def mouse_click(self, event):
        """ Проверяем, далеко ли шарик, и, если в него попали, то "лопаем" его,
            создаём новый шарик, а за старый начисляем очки.
        """
        pass  # FIXME

    def game_cycle(self, *ignore):
        canvas.after(dt, self.game_cycle)  # перезапуск цикла
        # FIXME: что-то делаем с шариком


class Ball:
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r
        self.avatar = canvas.create_image(x - r, y - r, image=ball_sprite)
        pass  #FIXME!

root_window = Tk()
ball_sprite = PhotoImage(file=ball_sprite_filename)
window = MainWindow(root_window)
root_window.mainloop()

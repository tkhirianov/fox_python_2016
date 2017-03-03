from tkinter import *
from random import *

screen_width = 600
screen_height = 400
r_min = 20
r_max = 50
dt = 10  # микросекунд
#ball_sprite_filename = "ball_sprite.png"
scores_format = 'очки: %d'


class MainWindow:
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()

        self.ball = Ball.generate_random_ball()
        self.scores = 0
        self.scores_text = canvas.create_text(screen_width - 50, 10,
                                              text=scores_format%self.scores)

        self.game_cycle()  # запуск игрового цикла
        canvas.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        """ Проверяем, далеко ли шарик, и, если в него попали, то "лопаем" его,
            создаём новый шарик, а за старый начисляем очки.
        """
        if self.ball.check_contact(event.x, event.y):
            self.scores += self.ball.scores
            canvas.itemconfig(self.scores_text, text=scores_format%self.scores)
            self.scores_text
            self.ball.destroy()
            self.ball = Ball.generate_random_ball()

    def game_cycle(self, *ignore):
        canvas.after(dt, self.game_cycle)  # перезапуск цикла
        if self.ball is not None:
            self.ball.move()


class Ball:
    def __init__(self, x, y, r, Vx=0, Vy=0):
        self.x, self.y, self.r = x, y, r
        self.Vx, self.Vy = Vx, Vy
        self.avatar = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
        self.scores = 10 + r_max - r

    def check_contact(self, x, y):
        l = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return l <= self.r

    def destroy(self):
        canvas.delete(self.avatar)

    def move(self):
        """ сдвинуть шарик на его скорость """
        # FIXME
        self.x += 1
        canvas.move(self.avatar, 1, 0)
        pass

    @classmethod
    def generate_random_ball(cls):
        r = randint(r_min, r_max)
        x = randint(r, screen_width-r-1)
        y = randint(r, screen_height-r-1)
        # FIXME: добавить генерацию случайной скорости
        return Ball(x, y, r)


root_window = Tk()
#ball_sprite = PhotoImage(file=ball_sprite_filename)
window = MainWindow(root_window)
root_window.mainloop()

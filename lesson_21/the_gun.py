from tkinter import *
from random import *

screen_width = 600
screen_height = 400
r_min = 20
r_max = 50
dt = 0.1  # физический шаг времени между кадрами обсчёта
V_max = 50
fps = 20  # количество кадров в секунду
sleep_time = round(1000/fps)
#ball_sprite_filename = "ball_sprite.png"
scores_format = 'очки: %d'


class MainWindow:
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()

        self.target = Target.generate_random()
        self.scores = 0
        self.scores_text = canvas.create_text(screen_width - 50, 10,
                                              text=scores_format%self.scores)

        self.game_cycle()  # запуск игрового цикла
        canvas.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        """ Проверяем, далеко ли шарик, и, если в него попали, то "лопаем" его,
            создаём новый шарик, а за старый начисляем очки.
        """
        if self.target.check_contact(event.x, event.y):
            self.scores += self.target.scores
            canvas.itemconfig(self.scores_text, text=scores_format%self.scores)
            self.target.destroy()
            self.target = Target.generate_random()

    def game_cycle(self, *ignore):
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла
        if self.target is not None:
            self.target.move()


class Ball:
    def __init__(self, x, y, r, Vx, Vy, color):
        self.x, self.y, self.r = x, y, r
        self.Vx, self.Vy = Vx, Vy
        self.avatar = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)

    def check_contact(self, x, y):
        l = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return l <= self.r

    def destroy(self):
        canvas.delete(self.avatar)

    def move(self):
        """ сдвинуть шарик на его скорость """
        ax = 0
        ay = 10
        self.x += self.Vx*dt  # Добавить поправку?!
        self.y += self.Vy*dt
        self.Vx += ax*dt
        self.Vy += ay*dt
        canvas.coords(self.avatar, self.x-self.r, self.y-self.r,
                      self.x+self.r, self.y+self.r)


class Shell(Ball):
    def __init__(self, x, y, r, Vx, Vy):
        super().__init__(x, y, r, Vx, Vy, "red")


class Target(Ball):
    def __init__(self, x, y, r, Vx=0, Vy=0):
        super().__init__(x, y, r, Vx, Vy, "green")
        self.scores = 10 + r_max - r

    @classmethod
    def generate_random(cls):
        r = randint(r_min, r_max)
        x = randint(r, screen_width-r-1)
        y = randint(r, screen_height-r-1)
        # генерация случайной скорости
        Vx = randint(-V_max, +V_max)
        Vy = randint(-V_max, +V_max)
        return Target(x, y, r, Vx, Vy)


root_window = Tk()
#ball_sprite = PhotoImage(file=ball_sprite_filename)
window = MainWindow(root_window)
root_window.mainloop()

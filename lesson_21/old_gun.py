from tkinter import *
from random import *

frame_sleep_time = 10  # задержка между кадрами в милисекундах
dt = 0.1  # квант игрового времени между кадрами
g = 9.8    # гравитационная постоянная игры


def create_scores_text():
    global scores_text
    scores_text = canvas.create_text(60, 12, text="Scores: " + str(scores),
                                     font="Sans 18")


def change_scores_text():
    canvas.itemconfigure(scores_text, text="Scores: " + str(scores))


def random_color():
    colors = ["green", "red", "blue", "yellow", "magenta", "cyan", "black"]
    return choice(colors)


class Ball:
    def __init__(self):
        self.r = randint(10, 50)
        self.x, self.y = self.generate_random_ball_coord()
        self.vx, self.vy = self.generate_random_ball_velocity()
        self.avatar = canvas.create_oval(self.x - self.r, self.y - self.r,
                                         self.x + self.r, self.y + self.r, fill=random_color())

    def move(self):
        new_x = self.x + self.vx*dt
        new_y = self.y + self.vy*dt + g*dt**2/2
        self.vy += g*dt
        if new_x < self.r or new_x > screen_width - self.r:
            new_x = self.x  # rolling back coordinate!
            self.vx = -self.vx
        if new_y < self.r or new_y > screen_height - self.r:
            new_y = self.y  # rolling back coordinate!
            self.vy = -self.vy
        canvas.move(self.avatar, new_x - self.x, new_y - self.y)
        self.x, self.y = new_x, new_y

    def flick(self):
        new_x, new_y = self.generate_random_ball_coord()
        self.vx, self.vy = self.generate_random_ball_velocity()
        canvas.move(self.avatar, new_x - self.x, new_y - self.y)
        self.x, self.y = new_x, new_y

    def generate_random_ball_coord(self):
        x = randint(self.r, screen_width - self.r)
        y = randint(self.r, screen_height - self.r)
        return x, y

    def generate_random_ball_velocity(self):
        vx = randint(-10, +10)
        vy = randint(-10, +10)
        return vx, vy

    def check_collision(self, x, y):
        return (x - self.x)**2 + (y - self.y)**2 <= self.r**2


class Bullet(Ball):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.r = 10
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        canvas.coords(self.avatar, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        # FIXME: fill="black"
        print('bullet:', x, y, vx, vy)


class Cannon:
    def __init__(self):
        self.x = 0
        self.y = screen_height
        self.lx = 30
        self.ly = 30
        self.avatar = canvas.create_line(self.x, self.y, self.x + self.lx,
                                         self.y - self.ly, fill="black", width=3)

    def shoot(self):
        vx = self.lx
        vy = self.ly
        return Bullet(self.x + self.lx, self.y + self.ly, vx, vy)

    def aim(self, x, y):
        l = ((x - self.x)**2 + (y - self.y)**2)**0.5
        self.lx = 40*(x - self.x)/l
        self.ly = 40*(y - self.y)/l
        canvas.coords(self.avatar, self.x, self.y, self.x + self.lx, self.y + self.ly)


def time_event():
    global scores

    # даём возможность подвинуться всем целям
    for target in targets:
        target.move()
    # если снаряд существует, то он летит
    if bullet:   # FIXME сделать много снарядов
        bullet.move()
        # проверка, не столкнулся ли снаряд с целью
        for target in targets:
            if target.check_collision(bullet.x, bullet.y):
                target.flick()
                scores += 1
                change_scores_text()

    canvas.after(frame_sleep_time, time_event)

def mouse_move(event):
    # целимся пушкой на курсор
    cannon.aim(event.x, event.y)


def mouse_click(event):
    global bullet
    if bullet:
        canvas.delete(bullet.avatar)
    bullet = cannon.shoot()
    print(bullet.avatar)


root = Tk()
canvas = Canvas(root)
canvas.pack()

scores = 0
screen_width = int(canvas["width"])
screen_height = int(canvas["height"])

targets = [Ball() for i in range(5)]
bullet = None
cannon = Cannon()

create_scores_text()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Motion>', mouse_move)
time_event()  # начинаю циклически запускать таймер
root.mainloop()

from math import *
from tkinter import *
from random import *
from enum import Enum

blocks_horizontal_number = 20
blocks_vertical_number = 40
block_width = 30
block_height = 10
screen_width = block_width*blocks_horizontal_number
screen_height = block_height*blocks_vertical_number

dt = 0.1  # физический шаг времени между кадрами обсчёта
fps = 20  # количество кадров в секунду
sleep_time = round(1000/fps)
#ball_sprite_filename = "ball_sprite.png"
scores_format = 'очки: %d'


class GameState(Enum):
    BALL_IS_ON_PLATFORM = 1
    BALL_IS_FLYING = 2
    GAME_OVER = 3


class MainWindow:
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()

        self.blocks = []
        self.platform = Platform()
        self.balls = [Ball(self.platform.x, screen_height - self.platform.height - 5,
                           5, 10, -10, 'green')]
        self.scores = 0
        self.scores_text = canvas.create_text(screen_width - 50, 10,
                                              text=scores_format%self.scores)
        canvas.bind("<Button-1>", self.mouse_click)
        canvas.bind("<Motion>", self.mouse_motion)
        self.game_state = GameState.BALL_IS_FLYING

    def mouse_motion(self, event):
        if self.game_state == GameState.GAME_OVER:
            return  # ничего не делаем
        x, y = event.x, event.y
        self.platform.aim(x, y)

    def mouse_click(self, event):
        """ Проверяем, далеко ли шарик, и, если в него попали, то "лопаем" его,
            создаём новый шарик, а за старый начисляем очки.
        """
        if self.game_state != GameState.BALL_IS_ON_PLATFORM:
            return  # ничего не делаем
        #platform.shoot(x, y)

    def shell_flying(self, *ignore):
        if self.game_state != GameState.SHELL_IS_FLYING:
            return  # ничего не делаем

        canvas.after(sleep_time, self.shell_flying)  # перезапуск цикла

        # смещаем цели и снаряды
        for ball in self.balls:
            ball.move()
        # проверяем столкновение снаряда с платформой
        # FIXME
        # проверяем столкновение снаряда с блоками
        # FIXME


class Ball:
    def __init__(self, x, y, r, Vx, Vy, color):
        self.x, self.y, self.r = x, y, r
        self.Vx, self.Vy = Vx, Vy
        self.avatar = canvas.create_oval(x-r, y-r,
                                         x+r, y+r, fill=color)

    def check_contact(self, x, y):
        l = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return l <= self.r

    def destroy(self):
        canvas.delete(self.avatar)

    def move(self):
        """ сдвинуть шарик на его скорость """
        self.x += self.Vx*dt
        self.y += self.Vy*dt
        # отражения слева, справа, снизу
        if self.x - self.r <= 0:
            self.Vx = -self.Vx
            self.x = self.r + 1
        if self.x + self.r >= screen_width:
            self.Vx = -self.Vx
            self.x = screen_width - self.r - 1
        if self.y + self.r <= 0:
            self.Vy = -self.Vy
            self.y = self.r + 1

        x1, y1 = self.x-self.r, self.y-self.r
        x2, y2 = self.x+self.r, self.y+self.r
        canvas.coords(self.avatar, x1, y1, x2, y2)


class Platform:
    default_width = 40
    height = 9

    def __init__(self):
        self.x = screen_width//2
        self.width = Platform.default_width
        self.line = canvas.create_line(self.x-self.width//2, screen_height-5,
                                       self.x+self.width//2, screen_height-5,
                                       width=Platform.height, fill='brown')

    def aim(self, x, y):
        # Ограничения, чтобы платформа не выезжала за границу игрового экрана
        if x < self.width//2:
            x = self.width//2
        if x > screen_width - self.width//2:
            x = screen_width - self.width//2

        self.x = x
        canvas.coords(self.line, self.x-self.width//2, screen_height-5,
                                       self.x+self.width//2, screen_height-5)

    def shoot(self, x, y):
        pass  #FIXME  необходимо только для 1-го этапа игры, когда мячик отстреливается от платформы


root_window = Tk()
#ball_sprite = PhotoImage(file=ball_sprite_filename)
window = MainWindow(root_window)
root_window.mainloop()

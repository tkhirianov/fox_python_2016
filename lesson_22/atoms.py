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
target_initial_number = 5
target_max_number = 10
default_target_born_time = 5  # секунд
#ball_sprite_filename = "ball_sprite.png"
scores_format = 'очки: %d'


class MainWindow:
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()

        self.gun = Gun()
        self.shells = []
        self.targets = [Target.generate_random() for i in range(target_initial_number)]
        self.scores = 0
        self.scores_text = canvas.create_text(screen_width - 50, 10,
                                              text=scores_format%self.scores)
        self.target_born_time = default_target_born_time
        self.game_cycle()  # запуск игрового цикла
        canvas.bind("<Button-1>", self.mouse_click)
        canvas.bind("<Motion>", self.mouse_motion)

    def mouse_motion(self, event):
        self.gun.aim(event.x, event.y)

    def mouse_click(self, event):
        """ Проверяем, далеко ли шарик, и, если в него попали, то "лопаем" его,
            создаём новый шарик, а за старый начисляем очки.
        """
        shell = self.gun.shoot(event.x, event.y)
        self.shells.append(shell)

    def game_cycle(self, *ignore):
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла


        # смещаем атомы
        for atom in self.atoms:
            atom.move()
        # для каждого атома проверяем столкновение со всеми остальными (кроме уже проверенных ранее)
        for i in range(len(self.atoms)):
            for k in range(i+1, len(self.atoms)):
                atom1 = self.atoms[i]
                atom2 = self.atoms[k]
                if check_collision(atom1, atom2):
                    # Упругое столкновение
                    collide(atom1, atom2)


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
        ay = 0
        self.x += self.Vx*dt  # Добавить поправку?!
        self.y += self.Vy*dt
        self.Vx += ax*dt
        self.Vy += ay*dt
        # отражения слева, справа, снизу
        if self.x - self.r <= 0:
            self.Vx = -self.Vx
            self.x = self.r+1
        if self.x + self.r >= screen_width:
            self.Vx = -self.Vx
            self.x = screen_width - self.r - 1
        if self.y + self.r >= screen_height:
            self.Vy = -self.Vy
            self.y = screen_height - self.r - 1
        canvas.coords(self.avatar, self.x-self.r, self.y-self.r,
                      self.x+self.r, self.y+self.r)


class Atom(Ball):
    def __init__(self, x, y, r, Vx, Vy):
        super().__init__(x, y, r, Vx, Vy, "red")


def check_collision(atom1, atom2):
    l = ((atom1.x - atom2.x)**2 + (atom1.y - atom2.y)**2)**0.5
    return l <= atom1.r + atom2.r


def collide(atom1, atom2):
    lx, ly = atom2.x - atom1.x, atom2.y - atom1.y
    l = (lx**2 + ly**2)**0.5
    nx, ny = lx/l, ly/l
    # выделение компонент скорости атома 1:
    v1_parallel = atom1.vx*nx + atom1.vy*ny
    v1_parallel_x = v1_parallel*nx
    v1_parallel_y = v1_parallel*ny
    v1_perpendicular_x = atom1.vx - v1_parallel_x
    v1_perpendicular_y = atom1.vy - v1_parallel_y
    # выделение компонент скорости атома 2:
    v2_parallel = atom2.vx*nx + atom2.vy*ny
    v2_parallel_x = v2_parallel*nx
    v2_parallel_y = v2_parallel*ny
    v2_perpendicular_x = atom2.vx - v2_parallel_x
    v2_perpendicular_y = atom2.vy - v2_parallel_y



root_window = Tk()
window = MainWindow(root_window)
root_window.mainloop()

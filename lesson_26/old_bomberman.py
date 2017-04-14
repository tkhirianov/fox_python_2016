#Работающий прототип игры Bomberman на языке Python 3:
# License: GPLv3
__author__ = "Timofey Khirianov"

from tkinter import *

frame_sleep_time = 100   # задержка между кадрами в милисекундах


class Cell:
    width = 40
    height = 40
    cell_type_by_symbol = {' ': 0, '#': 1, '+': 2, '$': 3}  # by symbol in level text file
    cell_color_by_type = {0: 'white', 1: 'red', 2: 'orange', 3: 'yellow'}  # by cell_type

    def __init__(self, cell_type):
        self.cell_type = cell_type

    @property
    def cell_color(self):
        return Cell.cell_color_by_type[self.cell_type]

    def is_wall(self):
        return self.cell_type in {1, 2}

cells_horizontal_number = 21
cells_vertical_number = 15
max_physical_x = cells_horizontal_number
max_physical_y = cells_vertical_number
screen_width = Cell.width * cells_horizontal_number    # ширина игрового экрана
screen_height = Cell.height * cells_vertical_number    # высота игрового экрана


def screen_x(_physical_x):
    return round(_physical_x * Cell.width)


def screen_y(_physical_y):
    return round(_physical_y * Cell.height)


def physical_x(_screen_x):
    return _screen_x / Cell.width


def physical_y(_screen_y):
    return _screen_y / Cell.height


class Field:
    def __init__(self, field_file):
        """загружает поле с клетками из файла"""
        with open(field_file) as file:
            self.cells = [None] * cells_vertical_number
            self.avatars = [None] * cells_vertical_number
            for yi in range(cells_vertical_number):
                self.cells[yi] = [None] * cells_horizontal_number
                self.avatars[yi] = [None] * cells_horizontal_number
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    # любой символ, кроме пробела -- значикт соотв. клетка жива
                    cell_type = Cell.cell_type_by_symbol[line[xi]]
                    cell = Cell(cell_type)
                    self.cells[yi][xi] = cell
                    self.avatars[yi][xi] = canvas.create_rectangle(screen_x(xi), screen_y(yi),
                                                                   screen_x(xi+1), screen_y(yi+1),
                                                                   fill=cell.cell_color)


class Bomb:
    explosion_time = 10  # условных микросекунд

    def __init__(self, flame_length, timeout, x, y):
        self.flame_length = flame_length
        self.timeout = timeout
        self.x = x
        self.y = y
        self.avatar = canvas.create_oval(screen_x(x), screen_y(y),
                                         screen_x(x+1), screen_y(y+1),
                                         fill='black')
        self.flame_avatar = None

    def is_exploding(self):
        """последние explosion_time микросенкунд своей жизни
           бомба находится в статусе "взрывающаяся" """
        return 0 < self.timeout <= Bomb.explosion_time

    def is_finished(self):
        """ бомба считается отработавшей, когда timeout <= 0 """
        return self.timeout <= 0

    def tick(self):
        self.timeout -= 1

        if self.is_exploding() and self.avatar:
            canvas.delete(self.avatar)
            self.avatar = None
            oval1 = canvas.create_oval(screen_x(self.x), screen_y(self.y - self.flame_length),
                                       screen_x(self.x + 1), screen_y(self.y + self.flame_length + 1),
                                       fill='lightblue')
            oval2 = canvas.create_oval(screen_x(self.x - self.flame_length), screen_y(self.y),
                                       screen_x(self.x + self.flame_length + 1), screen_y(self.y + 1),
                                       fill='lightblue')
            self.flame_avatar = [oval1, oval2]

        elif self.is_finished() and self.flame_avatar:
            canvas.delete(self.flame_avatar[0])
            canvas.delete(self.flame_avatar[1])
            self.flame_avatar = None


class Bomberman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.avatar = canvas.create_oval(screen_x(self.x), screen_y(self.y),
                                         screen_x(self.x + 1), screen_y(self.y + 1),
                                         fill='green')
        self.speed = 1
        self.bomb_number = 3
        self.bomb_flame_length = 1
        self.bomb_timeout = 50

    def redraw(self):
        """ смещает аватар в текущую позицию """
        canvas.coords(self.avatar, screen_x(self.x), screen_y(self.y),
                         screen_x(self.x + 1), screen_y(self.y + 1))

    def up_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        if self.y == 0\
                or level.field.cells[self.y-1][self.x].is_wall():
            return
        self.y -= 1  # FIXME: реализовать плавность движения
        self.redraw()

    def down_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        if self.y == max_physical_y-1\
                or level.field.cells[self.y+1][self.x].is_wall():
            return
        self.y += 1  # FIXME: реализовать плавность движения
        self.redraw()

    def left_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        if self.x == 0 or level.field.cells[self.y][self.x-1].is_wall():
            return
        self.x -= 1  # FIXME: реализовать плавность движения
        self.redraw()

    def right_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        if self.x == max_physical_x-1 \
                or level.field.cells[self.y][self.x+1].is_wall():
            return
        self.x += 1  # FIXME: реализовать плавность движения
        self.redraw()

    def bomb_event(self, event):
        """ событие постановки бомбы """
        new_bomb = Bomb(self.bomb_flame_length, self.bomb_timeout, self.x, self.y)
        level.bombs.append(new_bomb)


class Level:
    def __init__(self, level_file):
        self.field = Field(level_file)
        self.bombs = [Bomb(3, 100, 5, 5)]
        man = Bomberman(0, 0)
        root.bind('<Up>', man.up_event)
        root.bind('<Down>', man.down_event)
        root.bind('<Left>', man.left_event)
        root.bind('<Right>', man.right_event)
        root.bind('<Insert>', man.bomb_event)
        self.units = [man]

    def calculate(self):
        """  """
        for bomb in self.bombs:
            bomb.tick()

        #FIXME: убирать из списка уже разорвавшиеся бомбы


def time_event():
    global scores
    # перевычислить состояние поля с клетками
    level.calculate()
    canvas.after(frame_sleep_time, time_event)


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    level = Level('map1.txt')


    time_event()  # начинаю циклически запускать таймер
    root.mainloop()

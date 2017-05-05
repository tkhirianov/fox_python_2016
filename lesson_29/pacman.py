import tkinter
from enum import Enum

cells_horizontal_number = 15
cells_vertical_number = 15
cell_width = cell_height = 20
screen_width = cell_width*cells_horizontal_number
screen_height = cell_height*cells_vertical_number
sprite_number = 4

fps = 60  # количество кадров в секунду
sleep_time = round(1000/fps)

map_file = 'map1.txt'


class GameState(Enum):
    STOP = 0
    PLAY = 1


class MainWindow:
    def __init__(self, parent):
        self.parent = parent

        self.filename = None
        self.dirty = False
        self.data = {}

        global canvas  # Холст - глобальное имя (уровня модуля)
        canvas = tkinter.Canvas(parent)
        canvas["height"] = screen_height
        canvas["width"] = screen_width

        canvas.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.level = Level(map_file)
        canvas.after(sleep_time, self.level.game_cycle)  # запуск цикла для обсчёта


def screen_x(_physical_x):
    return round(_physical_x * cell_width)


def screen_y(_physical_y):
    return round(_physical_y * cell_height)


def screenify(xi, yi, xi_old=None, yi_old=None, sprite_i=0):
    """Возвращает четыре координаты - положение левой верхней и правой нижней точек спрайта"""
    if xi_old is not None and yi_old is not None:
        xi = (xi*sprite_i + xi_old*(sprite_number - sprite_i))/sprite_number
        yi = (yi*sprite_i + yi_old*(sprite_number - sprite_i))/sprite_number
    x1 = int(xi*cell_width)
    y1 = int(yi*cell_height)
    x2 = int((xi+1)*cell_width)
    y2 = int((yi+1)*cell_height)
    return x1, y1, x2, y2


class Unit:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi
        self.avatar = canvas.create_oval(*screenify(xi, yi),
                                         fill='green', outline='black')


class Pacman(Unit):
    default_bombs_number = 5

    def __init__(self, xi, yi):
        super().__init__(xi, yi)
        self.max_bombs_number = Pacman.default_bombs_number
        self.bombs_number = self.max_bombs_number
        self.sprite_i = 0
        self.xi, self.yi = xi, yi
        self.xi_old, self.yi_old = self.xi, self.yi

    def step(self):
        self.sprite_i = (self.sprite_i + 1)%sprite_number
        #canvas.itemconfigure(self.avatar, fill='green', outline='black')
        x1, y1, x2, y2 = screenify(self.xi, self.yi, self.xi_old, self.yi_old, self.sprite_i)
        canvas.coords(self.avatar, x1, y1, x2, y2)


class Level:
    cell = {'#': 'red', ' ': 'lightgray', '.': 'gray', 'p': 'Pacman', '^': 'purple'}

    def __init__(self, level_file):
        """ загружает схему уровня из файла """
        with open(level_file) as file:
            self.field = [[None] * cells_horizontal_number for i in range(cells_vertical_number)]
            self.avatars = [[None]*cells_horizontal_number for i in range(cells_vertical_number)]
            for yi in range(cells_vertical_number):
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    symbol = line[xi]
                    if Level.cell[symbol] == 'Pacman':
                        self.player = Pacman(xi, yi)
                        symbol = ' '
                    self.field[yi][xi] = symbol
                    color = Level.cell[symbol]
                    self.avatars[yi][xi] = canvas.create_rectangle(*screenify(xi, yi),
                                                                   fill=color, outline='lightgray')

        canvas.bind('<Up>', self.up_event)
        canvas.bind('<Down>', self.down_event)
        canvas.bind('<Left>', self.left_event)
        canvas.bind('<Right>', self.right_event)
        self.game_state = GameState.PLAY

    def game_cycle(self, *ignore):
        if self.game_state != GameState.PLAY:
            return  # ничего не делаем
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла

        self.player.step()

    def show(self):
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                color = Level.cell[self.field[yi][xi]]
                canvas.itemconfigure(self.avatars[yi][xi], fill=color)

    def up_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        player = self.player
        if (player.yi == 0
                or self.field[player.yi-1][player.xi].is_wall()):
            return
        player.dy = -1

    def down_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        player = self.player
        if (player.yi == cells_vertical_number-1
                or self.field[player.yi+1][player.xi].is_wall()):
            return
        player.dy = +1

    def left_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        player = self.player
        if (player.xi == 0
                or self.field[player.yi][player.xi-1].is_wall()):
            return
        player.dx = -1

    def right_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        player = self.player
        if (player.xi == cells_horizontal_number-1
                or self.field[player.yi][player.xi+1].is_wall()):
            return
        player.dx = +1


def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

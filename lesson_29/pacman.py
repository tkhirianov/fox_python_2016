import tkinter
from enum import Enum

cells_horizontal_number = 15
cells_vertical_number = 15
cell_width = cell_height = 40
screen_width = cell_width*cells_horizontal_number
screen_height = cell_height*cells_vertical_number
sprite_number = 4

fps = 20  # количество кадров в секунду
sleep_time = round(1000/fps)

map_file = 'map1.txt'


class GameState(Enum):
    STOP = 0
    PLAY = 1


class MainWindow:
    def __init__(self, parent):
        self.parent = parent

        global canvas  # Холст - глобальное имя (уровня модуля)
        canvas = tkinter.Canvas(parent, background='lightgray')  # создание глобального холста
        canvas["height"] = screen_height
        canvas["width"] = screen_width
        canvas.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.level = Level(map_file) # загрузка карты из файла

        # привязка нажатий на клавиши к обработчику
        for event in '<Up>', '<Down>', '<Left>', '<Right>', '<space>':
            self.parent.bind(event, self.level.key_event)
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
        self.xi = xi
        self.yi = yi
        self.avatar = None


class Pacman(Unit):
    default_bombs_number = 5

    def __init__(self, xi, yi):
        super().__init__(xi, yi)
        self.max_bombs_number = Pacman.default_bombs_number
        self.bombs_number = self.max_bombs_number
        self.sprite_i = 0
        self.xi_old, self.yi_old = self.xi, self.yi
        self.avatar = canvas.create_oval(*screenify(xi, yi),
                                         fill='green', outline='black')
        self.dx = self.dy = 0
        self.plan = (0, 0)

    def step(self, field, level):
        """ Шаг пакмана на поле field.
        При этом поле field требуется, чтобы не "вшагнуть" в стену,
        а также для того, чтобы убирать с поля "корм".
        """
        if (self.dx == 0 and self.dy == 0) or self.sprite_i == 0:
            #учитываем self.plan изменения dx, dy, который был запланирован за время перехода
            self.dx, self.dy = self.plan
            # FIXME смена спрайта!
            self.sprite_i = 0
        else:  # ненулевой спрайт! Изменение направления движения
               # в этот момент может быть только на противоположное
            if self.plan != (0, 0) and self.plan == (-self.dx, -self.dy):
                self.dx, self.dy = self.plan
                # подмена новой и старой координат
                self.xi_old, self.xi = self.xi, self.xi_old
                self.yi_old, self.yi = self.yi, self.yi_old
                self.sprite_i = sprite_number - self.sprite_i # шаг спрайта зеркальный
                # FIXME смена спрайта!

        if self.sprite_i == 0:  # если спрайт нулевой, то осуществляем смещение положения пакмана на поле
            self.xi_old, self.yi_old = self.xi, self.yi
            if self.dx != 0 or self.dy != 0:  # если я собираюсь куда-то перемещаться, то
                self.xi, self.yi = self.xi + self.dx, self.yi + self.dy
                if (self.xi < 0 or self.yi < 0  # если вышли за границы поля
                    or self.xi >= cells_horizontal_number or self.yi >= cells_vertical_number
                    or field[self.yi][self.xi] == '#'):  # или "вшагнули" в стену, то
                    # восстановить координаты и сбросить dx и dy
                    self.xi, self.yi = self.xi_old, self.yi_old
                    self.dx = self.dy = 0
                    self.plan = (0, 0)
                else:
                    # только что успешно перешагнул на новую клетку!
                    if field[self.yi][self.xi] == ".":  # съедаем еду в клетке
                        #self.score += 10  # FIXME
                        #level.food -= 1
                        field[self.yi][self.xi] = " "
                        canvas.delete(level.avatars[self.yi][self.xi])

        x1, y1, x2, y2 = screenify(self.xi, self.yi, self.xi_old, self.yi_old, self.sprite_i)
        #print('step:', x1, y1, x2, y2, self.sprite_i)
        canvas.coords(self.avatar, x1, y1, x2, y2)
        self.sprite_i = (self.sprite_i + 1)%sprite_number


class Level:
    cell = {'#': 'red', ' ': 'lightgray', '.': 'orange', 'p': 'Pacman', '^': 'purple'}

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
                        pacman_coords = xi, yi
                        symbol = ' '
                    self.field[yi][xi] = symbol
                    color = Level.cell[symbol]
                    if symbol == '.':
                        x1, y1, x2, y2 = screenify(xi, yi)
                        x1, y1, x2, y2 = x1+cell_width//3, y1+cell_height//3, x2-cell_width//3, y2-cell_height//3
                        self.avatars[yi][xi] = canvas.create_oval(x1, y1, x2, y2,
                                                                  fill=color, outline='red')
                    elif symbol == '#' or symbol == "^":
                        self.avatars[yi][xi] = canvas.create_rectangle(*screenify(xi, yi),
                                                                       fill=color, outline='lightgray')
            self.player = Pacman(*pacman_coords)

        self.game_state = GameState.PLAY

    def game_cycle(self, *ignore):
        if self.game_state != GameState.PLAY:
            return  # ничего не делаем
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла

        self.player.step(self.field, self)

    def show(self):
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                color = Level.cell[self.field[yi][xi]]
                canvas.itemconfigure(self.avatars[yi][xi], fill=color)

    def key_event(self, event):
        """ принимает событие с клавиатуры и действует в соответствии с ним"""
        key = event.keysym
        if key == 'Up':
            self.player.plan = (0, -1)
        elif key == 'Down':
            self.player.plan = (0, +1)
        elif key == 'Left':
            self.player.plan = (-1, 0)
        elif key == 'Right':
            self.player.plan = (+1, 0)
        elif key == 'space':
            self.player.plan = (0, 0)

def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

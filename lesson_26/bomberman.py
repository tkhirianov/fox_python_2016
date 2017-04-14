import tkinter
from enum import Enum

cells_horizontal_number = 30
cells_vertical_number = 20
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

        menubar = tkinter.Menu(self.parent)
        self.parent["menu"] = menubar
        fileMenu = tkinter.Menu(menubar)
        for label, command, shortcut_text, shortcut in (
                ("New game...", None, "Ctrl+N", "<Control-n>"),
                ("Table or records...", None, "Ctrl+O", "<Control-o>")):
            fileMenu.add_command(label=label, command=command, underline=0,
                             accelerator=shortcut_text)
            self.parent.bind(shortcut, command)
        menubar.add_cascade(label="File", menu=fileMenu, underline=0)

        frame = tkinter.Frame(self.parent)

        global canvas  # Холст - глобальное имя (уровня модуля)
        canvas = tkinter.Canvas(frame)
        canvas["height"] = screen_height
        canvas["width"] = screen_width

        canvas.grid(row=1, column=0, sticky=tkinter.NSEW)

        self.statusbar = tkinter.Label(frame, text="Готов...", anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky=tkinter.EW)

        frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.level = Level(map_file)

        self.level.game_state = GameState.PLAY
        canvas.after(sleep_time, self.level.game_cycle)  # запуск цикла для обсчёта

    def clearStatusBar(self, *ignore):
        self.statusbar["text"] = ""

    def set_status(self, text, timeout=5000):
        self.statusbar["text"] = text
        self.statusbar.after(timeout, self.clearStatusBar)


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


class Bomberman(Unit):
    default_bombs_number = 5

    def __init__(self, xi, yi):
        super().__init__(xi, yi)
        self.max_bombs_number = Bomberman.default_bombs_number
        self.bombs_number = self.max_bombs_number
        self.sprite_i = 0
        self.xi_old, self.yi_old = self.xi, self.yi

    def put_bomb(self, level):
        if self.bombs_number < self.max_bombs_number and level.field[self.yi][self.xi] != 'B':
            self.bombs_number -= 1
            level.field[self.yi][self.xi] = 'B'
            bomb = Bomb(self.xi, self.yi)
            level.bombs.append(bomb)

    def step(self):
        self.sprite_i = (self.sprite_i + 1)%sprite_number
        #canvas.itemconfigure(self.avatar, fill='green', outline='black')
        x1, y1, x2, y2 = screenify(self.xi, self.yi, self.xi_old, self.yi_old, self.sprite_i)
        canvas.coords(self.avatar, x1, y1, x2, y2)



class Level:
    cell = {'#': 'red', ' ': 'lightgray', 'm': 'Bomberman', 'B': 'Bomb'}

    def __init__(self, level_file):
        """ загружает схему уровня из файла """
        self.units = []
        with open(level_file) as file:
            self.field = [[None] * cells_horizontal_number for i in range(cells_vertical_number)]
            self.avatars = [[None]*cells_horizontal_number for i in range(cells_vertical_number)]
            for yi in range(cells_vertical_number):
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    symbol = line[xi]
                    if Level.cell[symbol] == 'Bomberman':
                        unit = Bomberman(xi, yi)
                        self.units.append(unit)
                        symbol = ' '
                    self.field[yi][xi] = symbol
                    color = Level.cell[symbol]
                    self.avatars[yi][xi] = canvas.create_rectangle(*screenify(xi, yi),
                                                                   fill=color, outline='lightgray')
        self.player = self.units[0]  # FIXME: пока считаем, что игрок один на поле
        # FIXME: события!!!
        canvas.bind('<Up>', self.up_event)
        canvas.bind('<Down>', self.down_event)
        canvas.bind('<Left>', self.left_event)
        canvas.bind('<Right>', self.right_event)
        canvas.bind('<Insert>', self.bomb_event)


    def game_cycle(self, *ignore):
        if self.game_state != GameState.PLAY:
            return  # ничего не делаем
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла

        for unit in self.units:
            unit.step()


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

    def bomb_event(self, event):
        """ событие постановки бомбы """
        new_bomb = self.player.put_bomb()
        self.bombs.append(new_bomb)


def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

# License: GPLv3
__author__ = "Timofey Khirianov"
from tkinter import *

frame_sleep_time = 500   # задержка между кадрами в милисекундах


class Cell:
    width = 40
    height = 40
    cell_type_by_symbol = {' ': 0, '#': 1, '.': 2, '^': 3}  # by symbol in level text file
    cell_color_by_type = {0: 'white', 1: 'orange', 2: 'yellow', 3: 'blue'}  # by cell_type

    def __init__(self, cell_type):
        self.cell_type = cell_type

    @property
    def cell_color(self):
        return Cell.cell_color_by_type[self.cell_type]

    def is_wall(self):
        return self.cell_type in {1}

cells_horizontal_number = 15
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


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.avatar = canvas.create_oval(screen_x(self.x), screen_y(self.y),
                                         screen_x(self.x + 1), screen_y(self.y + 1),
                                         fill='yellow')
        self.speed = 1

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


def ai_choice(monster_x, monster_y, field, pacman):
    """ ИИ, работающий на основе алгоритма заливки """
    # -1 в матрице длин кратчайших путей к клеткам значит, что клетка ещё не достигнута заливкой
    shortest_pathlen = [[-1]*cells_horizontal_number for line in range(cells_vertical_number)]
    shortest_pathlen[monster_y][monster_x] = 0
    queue = [(monster_x, monster_y)]

    while queue:  # пока в очереди на заливку ещё есть клетки
        x, y = queue.pop(0)  # берём из очереди первую клетку
        # перебираем все четыре соседние клетки
        for neighbour_x, neighbour_y in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            # если она не выходит за границу карты (1), не является стеной (2)
            # и при этом ещё не достигнута заливкой (3)
            if 0 <= neighbour_x < max_physical_x and 0 <= neighbour_y < max_physical_y and \
                    not level.field.cells[neighbour_y][neighbour_x].is_wall() and \
                    shortest_pathlen[neighbour_y][neighbour_x] == -1:
                # отмечаю ей длину кратчайшего пути как длину текущего кратчайшего + 1
                shortest_pathlen[neighbour_y][neighbour_x] = shortest_pathlen[y][x] + 1
                # и добавляю её в очередь на заливку
                queue.append((neighbour_x, neighbour_y))

    path = [(pacman.x, pacman.y)]  # построение пути начинаем с последней (целевой) клетки
    while path[-1] != (monster_x, monster_y):
        x, y = path[-1]
        # перебираем все четыре её соседние клетки
        for neighbour_x, neighbour_y in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            # если она не выходит за границу карты (1), и кратчайший путь в неё на 1 меньше текущего (2)
            if 0 <= neighbour_x < max_physical_x and 0 <= neighbour_y < max_physical_y and \
                    shortest_pathlen[neighbour_y][neighbour_x] == shortest_pathlen[y][x] - 1:
                # то добавляю её в кратчайший путь
                path.append((neighbour_x, neighbour_y))
                # и выходим из цикла for
                break
    path[:] = path[::-1]  # разворачиваю путь наоборот

    if len(path) == 1:
        return 0, 0  # вырожденный случай -- монстр на той же клетке, что и пакман
    else:
        x0, y0 = path[0]
        x1, y1 = path[1]
        return x1-x0, y1-y0

class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.avatar = canvas.create_oval(screen_x(self.x), screen_y(self.y),
                                         screen_x(self.x + 1), screen_y(self.y + 1),
                                         fill='cyan')
        self.speed = 1

    def redraw(self):
        """ смещает аватар в текущую позицию """
        canvas.coords(self.avatar, screen_x(self.x), screen_y(self.y),
                         screen_x(self.x + 1), screen_y(self.y + 1))

    def go(self, field, pacman):
        """ принимает решение о движении в ту или иную клетку и идёт туда"""
        dx, dy = ai_choice(self.x, self.y, field, pacman)
        self.x += dx
        self.y += dy
        self.redraw()


class Spawner:
    def __init__(self, x, y, monsters_number = 3, timer_value = 10):
        self.x = x
        self.y = y
        self.monsters_number = monsters_number
        self.timer_value = timer_value
        self.timer = self.timer_value

    def tick(self, level):
        """ считает такты по времени до рождения следующего монстра """
        # если монстров больше не нужно, то выходим
        if self.monsters_number == 0:
            return
        self.timer -= 1
        if self.timer <= 0:
            new_monster = Monster(self.x, self.y)  # порождаем нового монстра
            level.monsters.append(new_monster)  # добавляем его в список монстров
            self.monsters_number -= 1  # уменьшаем счётчик ещё не порождённых монстров
            self.timer = self.timer_value  # перезапускаем таймер

    @classmethod
    def load_level(self, level_file):
        """ загружает из файла поля список клеток, порождающих монстров """
        spawners = []
        with open(level_file) as file:
            for yi in range(cells_vertical_number):
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    cell_type = Cell.cell_type_by_symbol[line[xi]]
                    if cell_type == 3:  # 3 -- это spawner
                        spawner = Spawner(xi, yi)
                        spawners.append(spawner)
        return spawners

class Level:
    def __init__(self, level_file):
        self.field = Field(level_file)

        self.pacman = Pacman(1, 1)
        root.bind('<Up>', self.pacman.up_event)
        root.bind('<Down>', self.pacman.down_event)
        root.bind('<Left>', self.pacman.left_event)
        root.bind('<Right>', self.pacman.right_event)
        self.monsters = []
        self.spawners = Spawner.load_level(level_file)

    def calculate(self):
        """  """
        for spawner in self.spawners:
            spawner.tick(self)
        for monster in self.monsters:
            monster.go(self.field, self.pacman)


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

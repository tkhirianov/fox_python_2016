import tkinter
from enum import Enum

cells_horizontal_number = 30
cells_vertical_number = 30
cell_width = cell_height = 20
screen_width = cell_width*cells_horizontal_number
screen_height = cell_height*cells_vertical_number

fps = 1  # количество кадров в секунду
sleep_time = round(1000/fps)


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
                ("New...", self.fileNew, "Ctrl+N", "<Control-n>"),
                ("Open...", self.fileOpen, "Ctrl+O", "<Control-o>"),
                ("Save", self.fileSave, "Ctrl+S", "<Control-s>")):
            fileMenu.add_command(label=label, command=command, underline=0,
                             accelerator=shortcut_text)
            self.parent.bind(shortcut, command)
        menubar.add_cascade(label="File", menu=fileMenu, underline=0)

        frame = tkinter.Frame(self.parent)
        self.toolbar_images = []
        toolbar = tkinter.Frame(frame)

        for image, command in (
                ("filenew.gif", self.fileNew),
                ("fileopen.gif", self.fileOpen),
                ("filesave.gif", self.fileSave)):
            image = tkinter.PhotoImage(file=image)
            self.toolbar_images.append(image)
            button = tkinter.Button(toolbar, image=image, command=command)
            button.grid(row=0, column=len(self.toolbar_images)-1)

        toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NW)

        global canvas  # Холст - глобальное имя (уровня модуля)
        canvas = tkinter.Canvas(frame)
        canvas["height"] = screen_height
        canvas["width"] = screen_width

        canvas.grid(row=1, column=0, sticky=tkinter.NSEW)

        self.statusbar = tkinter.Label(frame, text="Готов...", anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky=tkinter.EW)

        frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.field = Field('map1.txt')

        self.game_state = GameState.PLAY
        canvas.after(sleep_time, self.game_cycle)  # запуск цикла для обсчёта

    def game_cycle(self, *ignore):
        if self.game_state != GameState.PLAY:
            return  # ничего не делаем
        canvas.after(sleep_time, self.game_cycle)  # перезапуск цикла
        self.field.next_step()
        self.field.show()

    def fileNew(self, *ignore):
        self.set_status('New File!')

    def fileOpen(self, *ignore):
        self.set_status('Open File!')


    def fileSave(self, *ignore):
        self.set_status('Save File!')

    def clearStatusBar(self, *ignore):
        self.statusbar["text"] = ""

    def set_status(self, text, timeout=5000):
        self.statusbar["text"] = text
        self.statusbar.after(timeout, self.clearStatusBar)


class Field:
    color = {'1': 'darkgreen', ' ': 'white',
             1: 'darkgreen',   0: 'white'}

    def __init__(self, level_file):
        """ загружает схему кирпичей уровня из файла """
        with open(level_file) as file:
            self.matrix = [[None]*cells_horizontal_number for i in range(cells_vertical_number)]
            self.avatars = [[None]*cells_horizontal_number for i in range(cells_vertical_number)]
            for yi in range(cells_vertical_number):
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    color = Field.color[line[xi]]
                    self.matrix[yi][xi] = 1 if (line[xi] == '1') else 0
                    self.avatars[yi][xi] = canvas.create_rectangle(xi*cell_width, yi*cell_height,
                                                                   (xi+1)*cell_width, (yi+1)*cell_height,
                                                                   fill=color)

    def next_step(self):
        new_map = [[0]*cells_horizontal_number for i in range(cells_vertical_number)]
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                neighbours = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        neighbours += self.matrix[yi+dy][xi+dx]
                cell_state = self.matrix[yi][xi]
                neighbours -= cell_state
                if cell_state == 1 and 2 <= neighbours <= 3:
                    new_map[yi][xi] = 1
                elif cell_state == 0 and neighbours == 3:
                    new_map[yi][xi] = 1
                else:
                    new_map[yi][xi] = 0
        self.matrix = new_map

    def show(self):
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                color = Field.color[self.matrix[yi][xi]]
                canvas.itemconfigure(self.avatars[yi][xi], fill=color)

def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

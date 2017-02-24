from tkinter import *
dt = 50


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=400, bg='lightgreen')
        self.canvas.pack()
        self.a = [300, 200]
        self.line = self.canvas.create_line(self.a, [400, 200], width=5, fill='red')
        self.ball = self.canvas.create_oval(0, 0, 40, 40)

        self.canvas.bind('<Motion>', self.mouse_motion)
        self.canvas.after(dt, self.game_cycle)
        self.root.mainloop()

    def mouse_motion(self, event):
        b = [event.x, event.y]
        self.canvas.coords(self.line, *self.a, *b)

    def game_cycle(self, *ignore):
        print('Очередная итерация игры')
        self.canvas.move(self.ball, 1, 1)

        self.canvas.after(dt, self.game_cycle)  # перезапуск цикла

window = MainWindow()

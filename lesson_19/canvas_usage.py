from tkinter import *
dt = 50
ball_radius = 10


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=400, bg='lightgreen')
        self.canvas.pack()
        self.a = [300, 200]
        self.line = self.canvas.create_line(self.a, [400, 200], width=5, fill='red')
        self.balls = []
        self.balls_velocity = []
        self.ball_sprite = PhotoImage(file="ball_sprite.png")

        self.canvas.bind('<Motion>', self.mouse_motion)
        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.after(dt, self.game_cycle)
        self.root.mainloop()

    def mouse_motion(self, event):
        b = [event.x, event.y]
        self.canvas.coords(self.line, *self.a, *b)

    def mouse_click(self, event):
        #ball = self.canvas.create_oval(event.x - ball_radius, event.y - ball_radius,
        #                               event.x + ball_radius, event.y + ball_radius)
        ball = self.canvas.create_image(event.x - ball_radius, event.y - ball_radius,
                                        image=self.ball_sprite, tag='ball')
        vx = round((event.x - self.a[0])/10)
        vy = round((event.y - self.a[1])/10)
        self.balls_velocity.append([vx, vy])
        self.balls.append(ball)

    def game_cycle(self, *ignore):
        self.canvas.after(dt, self.game_cycle)  # перезапуск цикла
        for ball, velocity in zip(self.balls, self.balls_velocity):
            self.canvas.move(ball, velocity[0], velocity[1])


window = MainWindow()

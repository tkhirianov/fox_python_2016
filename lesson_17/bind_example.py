from tkinter import *


def handler(event):
    print(event.num, event.x, event.y)
    event.widget["text"] = 'МЕНЯ НАЖАЛИ'


def but_pressed():
    print('Кнопка нажата (т.е. отжата!)')

root = Tk()
but = Button(root, text='OK', width=20, height=20, command=but_pressed)
label = Label(root, text='Label')
but.pack()
label.pack()

but.bind('<Button>', handler)
label.bind('<Button>', handler)

root.mainloop()
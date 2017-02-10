from tkinter import *

def main():
    root = Tk()
    init_window(root)
    root.mainloop()


def init_window(root):
    # создаём все виджеты
    global replace_frame
    text = Text(root, width=30, height=10, font='12', wrap=WORD)
    replace_frame_show_button = Button(root, text='Отобразить фрейм', command=show_replace_frame)
    replace_frame = Frame(root, width=300, height=100, bg='blue')
    replace_entry1 = Entry(replace_frame, width=20)
    replace_entry2 = Entry(replace_frame, width=20)
    replace_button = Button(replace_frame, text='Заменить', width=10)
    
    # упаковываем
    text.pack(side=TOP)
    replace_frame_show_button.pack(side=TOP)
    replace_entry1.grid(row=0, column=0)
    replace_entry2.grid(row=0, column=1)
    replace_button.grid(row=1, column=0)

    # и привязываем события


def show_replace_frame():
    replace_frame.pack(side=BOTTOM)

main()

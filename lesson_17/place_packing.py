from tkinter import *

def main():
    root = Tk()
    init_window(root)
    root.mainloop()


def init_window(root):
    # создаём все виджеты
    text = Text(root, width=30, height=10, font='12', wrap=WORD)
    replace_entry1 = Entry(root, width=20)
    replace_entry2 = Entry(root, width=20)
    replace_button = Button(root, text='Заменить')
    
    # упаковываем
    text.place(x=5, y=5)
    replace_entry1.place(x=5, y=200)
    replace_entry2.place(x=140, y=200)
    replace_button.place(x=10, y=230)

    # и привязываем события





main()

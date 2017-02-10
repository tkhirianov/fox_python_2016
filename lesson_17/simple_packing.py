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
    text.pack(side=TOP)
    replace_entry1.pack(side=LEFT)
    replace_entry2.pack(side=RIGHT)
    replace_button.pack()

    # и привязываем события





main()

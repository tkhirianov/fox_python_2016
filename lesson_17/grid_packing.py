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
    text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    replace_entry1.grid(row=1, column=0, padx=5, pady=5)
    replace_entry2.grid(row=1, column=1, padx=5, pady=5)
    replace_button.grid(row=2, column=0, padx=5, pady=5)

    # и привязываем события





main()

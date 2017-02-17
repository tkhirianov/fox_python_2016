from tkinter import *

def main():
    global window
    window = MainWindow()
    window.mainloop()

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        # создаём все виджеты
        self.text = Text(self, width=30, height=10, font='12', wrap=WORD)
        self.replace_entry1 = Entry(self, width=20)
        self.replace_entry2 = Entry(self, width=20)
        self.replace_button = Button(self, text='Заменить', command=replace_handler)

        # упаковываем
        self.text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.replace_entry1.grid(row=1, column=0, padx=5, pady=5)
        self.replace_entry2.grid(row=1, column=1, padx=5, pady=5)
        self.replace_button.grid(row=2, column=0, padx=5, pady=5)


def replace_handler():
    search_string = window.replace_entry1.get()
    replace_string = window.replace_entry2.get()
    text = window.text.get('1.0', END)
    replaced_text = text.replace(search_string, replace_string)
    window.text.delete('1.0',END)
    window.text.insert('1.0', replaced_text)

main()

import tkinter

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

        scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
        self.listBox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listBox.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.listBox.focus_set()
        scrollbar["command"] = self.listBox.yview
        scrollbar.grid(row=1, column=1, sticky=tkinter.NS)


        frame.pack()


    def fileNew(self, *ignore):
        print('New File!')

    def fileOpen(self, *ignore):
        print('Open File!')

    def fileSave(self, *ignore):
        print('Save File!')


def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

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

        image = tkinter.PhotoImage(file=image)
        self.toolbar_images.append(image)

    def fileNew(self):
        pass

    def fileOpen(self):
        pass

    def fileSave(self):
        pass


def main():
    root = tkinter.Tk()
    main_window = MainWindow(root)
    root.mainloop()

main()

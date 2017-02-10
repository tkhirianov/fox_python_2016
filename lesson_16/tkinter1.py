from tkinter import *

count = 0

def button_event_handler():
    global count
    print('Нажали на кнопку')
    count += 1
    button["text"] = "нажали " + str(count) + " раз"


# главное оконо приложения    
root = Tk()

# кнопка обыкновенная
button = Button(root, text="Нажми меня!",   
                font="Arial 20", borderwidth=3, underline=True,
                command=button_event_handler)
button.pack()

# метка - текст для пояснений интерфейса
label = Label(root, text="Это - метка. Тут можно писать.\nДаже на второй строке")
label.pack()

# область ввода текста однострочная
entry = Entry(root, width=10)
entry.pack()

# многострочная область для ввода текста
textarea = Text(root, width=10, height=4)
textarea.pack()

# радиокнопка - СЕМЕЙСТВО радиокнопок
var = IntVar()
var.set(1)
var_label = Label(root, textvar=var)
var_label.pack()
radio0 = Radiobutton(root, text="Ноль", variable=var, value=0)
radio1 = Radiobutton(root, text="Один", variable=var, value=1)
radio2 = Radiobutton(root, text="Два", variable=var, value=2)
radio0.pack()
radio1.pack()
radio2.pack()

# кпопки с галочкой
var2 = IntVar()
var2.set(1)
var2_label = Label(root, textvar=var2)
var2_label.pack()
checkbutton = Checkbutton(root, text="Кнопка-флажок", variable=var2)
checkbutton.pack()

root.mainloop()

print('Конец программы. До свидания!')

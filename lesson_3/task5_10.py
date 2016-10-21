#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.loadmap('task5-10')
def task():
    pass
    #------- пишите код здесь -----
    # для каждой строки
    while r.freeDown():
        # закрасить строчку
        # вправо до упора с закраской
        r.paint()
        while r.freeRight():
            r.right()
            r.paint()
        # влево до упора
        while r.freeLeft():
            r.left()
        # перейти на следующую строчку
        r.down()
    # вправо до упора с закраской
    r.paint()
    while r.freeRight():
        r.right()
        r.paint()
    # влево до упора
    while r.freeLeft():
        r.left()

    #------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.right() - вправо
#r.down() - вниз
#r.up() - вверх
#r.left() - влево
#r.paint() - закрасить  Paint

#r.color() - закрашена ли клетка? Color
#r.freeRight() - свободно ли справа? freeRight
#r.freeLeft() - свободно ли слева?  freeLeft
#r.freeUp() - свободно ли сверху? freeUp
#r.freeDown() - свободно ли снизу?  freeDown

#r.wallRight() - стена ли справа? wallRight
#r.wallLeft() - стена ли слева?  wallLeft
#r.wallUp() - стена ли сверху? wallUp
#r.wallDown() - стена ли снизу?  wallDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый

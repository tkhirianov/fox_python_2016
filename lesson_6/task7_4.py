#-*- coding: utf-8 -*
import robot

def measure_left():
    steps = 0
    while r.freeLeft():
        r.left()
        steps += 1
    r.right(steps)
    return steps

def measure_right():
    steps = 0
    while r.freeRight():
        r.right()
        steps += 1
    r.left(steps)
    return steps


def task():
    pass
    r.sleep = 0.1
    #------- пишите код здесь -----
    x = measure_left()
    y = measure_right()
    if x < y:
        r.left(x)
    else:
        r.right(y)
    #------- пишите код здесь -----

r = robot.rmap()
r.loadmap('task7-4')
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

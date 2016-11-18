#-*- coding: utf-8 -*
import robot

def box(n, m):
    """ рисует прямоугольник из
        n строк и m клеток в строке
    """
    for line in range(n):
        for cell in range(m):
            r.paint()
            r.right()
        r.left(m)
        r.down()
    r.up(n)

def task():
    pass
    r.sleep = 0.01
    #------- пишите код здесь -----
    r.right()
    r.down()
    box(3, 6)
    r.right(8)
    box(4, 9)
    r.right(10)
    box(12, 4)
    r.left(18)
    r.down(6)
    box(6, 4)
    r.right(8)
    box(6, 6)
    r.left(9)
    r.up(7)
    #------- пишите код здесь -----

r = robot.rmap()
r.loadmap('task4-16')
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

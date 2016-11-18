#-*- coding: utf-8 -*
import robot

def flower():
    """ рисует цветочек
        справа-внизу от текущей клетки
        и возвращается в исходную клетку
    """
    r.right()
    r.paint()
    r.down()
    r.paint()
    r.down()
    r.paint()
    r.right()
    r.up()
    r.paint()
    r.left()
    r.left()
    r.paint()
    r.up()

def task():
    pass
    #------- пишите код здесь -----
    r.right()
    r.down()
    flower()
    #------- пишите код здесь -----

r = robot.rmap()
r.loadmap('task2-1')
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

#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.loadmap('task7-3')
def task():
    pass
    #------- пишите код здесь -----
    steps_down = 0
    while r.freeDown():
        r.down()
        steps_down += 1
        r.settext(steps_down)

    # обойдём стену справа:
    steps_right = 0
    while r.wallDown():
        r.right()
        steps_right += 1
        r.settext(steps_right)
    r.down()
    for i in range(steps_right):
        r.left()
        r.settext(i+1)
    # а теперь вниз steps_down раз
    for i in range(steps_down):
        r.down()
        r.settext(i+1)
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

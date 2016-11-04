#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.loadmap('task7-4')
def task():
    pass
    #------- пишите код здесь -----
    
    # сбегаем к стене справа:
    steps_right = 0
    while r.freeRight():
        r.right()
        steps_right += 1
        r.settext(steps_right)  # DEBUG PRINT
    for i in range(steps_right):
        r.left()

    # а теперь сбегаем к стене слева:
    steps_left = 0
    while r.freeLeft():
        r.left()
        steps_left += 1
        r.settext(steps_left)  # DEBUG PRINT
    for i in range(steps_left):
        r.right()

    # решаем куда идти - налево или направо
    if steps_left < steps_right:
        r.left(steps_left)
    else:
        r.right(steps_right)
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

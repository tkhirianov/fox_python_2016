from random import randint

def game_help():
    """ обучающая игра для детей 7-10 лет
     для проверки умения совершать арифметические действия в уме
     текстовая игра типа "вопрос-ответ"
     герой встречает на пути трёх "драконов",
     каждый из которых спрашивает примеры на свой тип действий
     правильный ответ - это удар по дракону
     неправильный - удар по игроку
     когда игрок теряет всё здоровье, игра заканчивается"""


class Dragon:
    def __init__(self, health, damage, color):
        self.health = health
        self.damage = damage
        self.color = color
        
    def check_answer(self, player_answer):
        return self.answer == int(player_answer)
    

class GreenDragon(Dragon):
    """ проверяет операцию сложения """
    
    def __init__(self):
        super().__init__(30, 5, 'зелёный')

    def question(self):
        """ возвращает вопрос в качестве строки
            при этом сам дракон запоминает ответ как число"""
        x = randint(1, 20)
        y = randint(1, 20)
        self.answer = x + y
        return str(x) + '+' + str(y) + '='


class RedDragon(Dragon):
    """ проверяет операцию вычитания """
    
    def __init__(self):
        super().__init__(40, 10, 'красный')

    def question(self):
        """ возвращает вопрос в качестве строки
            при этом сам дракон запоминает ответ как число"""
        x = randint(1, 20)
        y = randint(1, x)
        self.answer = x - y
        return str(x) + '-' + str(y) + '='


class BlackDragon(Dragon):
    """ проверяет операцию сложения """
    
    def __init__(self):
        super().__init__(50, 15, 'чёрный')

    def question(self):
        """ возвращает вопрос в качестве строки
            при этом сам дракон запоминает ответ как число"""
        x = randint(1, 10)
        y = randint(1, 10)
        self.answer = x * y
        return str(x) + '*' + str(y) + '='


class Player:
    def __init__(self):
        self.health = 100
        self.damage = 10


def game():
    player = Player()
    dragons = [BlackDragon(), RedDragon(), GreenDragon()]
    while dragons:
        dragon = dragons.pop()
        print('На вас напал', dragon.color, 'дракон')
        while dragon.health > 0:  # пока дракон жив
            question = dragon.question()
            answer = input(question)
            correct = dragon.check_answer(answer)
            if correct:
                dragon.health -= player.damage
                print('Вы ударили дракона!')
            else:
                player.health -= dragon.damage
                print('Вы получили удар...')
            if player.health <= 0:
                print('Вы погибли... Конец игры!')
                return
        print(dragon.color.title(), 'дракон повержен!')
    print('Поздравляем! Вы победили всех драконов!')


if __name__ == '__main__':
    game()

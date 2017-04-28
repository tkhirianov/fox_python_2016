player_symbols = ['X', 'O']
enemy = {'X': 'O', 'O': 'X'}


class Field:
    def __init__(self):
        self.m = "."*9

    def __str__(self):
        return (self.m[0:3] + '\n' +
                self.m[3:6] + '\n' +
                self.m[6:9] + '\n')

    def check_win(self, symbol):
        win = False
        # горизонтали:
        win = win or (self.m[0:3] == 3*symbol)
        win = win or (self.m[3:6] == 3*symbol)
        win = win or (self.m[6:9] == 3*symbol)
        # вертикали:
        win = win or (self.m[0::3] == 3*symbol)
        win = win or (self.m[1::3] == 3*symbol)
        win = win or (self.m[2::3] == 3*symbol)
        # диагонали
        win = win or (self.m[0::4] == 3*symbol)
        win = win or (self.m[2:7:2] == 3*symbol)
        return win

    def game_over(self):
        if self.check_win("X") or self.check_win("O"):
            return True
        return self.m.find(".") == -1 # ничья - все позиции заняты

    def paint(self, choice, symbol):
        self.m = self.m[:choice] + symbol + self.m[choice+1:]

    def unpaint(self, choice):
        self.m = self.m[:choice] + '.' + self.m[choice+1:]


    def cell_free(self, choice):
        return self.m[choice] == '.'

    def choice_score(self, choice, player):
        self.paint(choice, player)
        if self.check_win(player):
            score = +1
        elif self.game_over():
            score = 0
        else: # рекуррентный случай
            worst_score = 10
            for enemy_choice in range(9):
                if self.cell_free(enemy_choice):
                    choice_score = self.choice_score(enemy_choice, enemy[player])
                    if choice_score < worst_score:
                        worst_score = choice_score
            score = -worst_score

        self.unpaint(choice)
        return score


def human_choice(field, player):
    choice = int(input("Ваш ход [0-8]:"))
    while not field.cell_free(choice):
        choice = int(input("Клетка занята. Ваш ход [0-8]:"))
    return choice


def ai_choice(field, player):
    assert not field.game_over(), "Невозможно делать ход в состоянии конца игры!"

    best_choice = None
    worst_score = +10
    for choice in range(9):
        if field.cell_free(choice):
            score = field.choice_score(choice, player)
            print("DEBUG:", choice, score)
            if score < worst_score:
                worst_score = score
                best_choice = choice
    return best_choice


def tournament():
    field = Field()
    while not field.game_over():
        print(field)
        choice = human_choice(field, "X")
        field.paint(choice, "X")
        if field.game_over():
            break
        print(field)
        choice = ai_choice(field, "O")
        field.paint(choice, "O")

    if field.check_win("X"):
        print("Крестики выиграли!")
    elif field.check_win("O"):
        print("Нолики выиграли!")
    else:
        print("Ничья.")


if __name__ == "__main__":
    tournament()

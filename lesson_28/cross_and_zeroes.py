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


def human_choice(field, symbol):
    choice = int(input("Ваш ход [0-8]:"))
    while field.m[choice] != ".":
        choice = int(input("Клетка занята. Ваш ход [0-8]:"))
    return choice


def tournament():
    field = Field()
    while not field.game_over():
        print(field)
        choice = human_choice(field, "X")
        field.paint(choice, "X")
        if field.game_over():
            break
        print(field)
        choice = human_choice(field, "O")
        field.paint(choice, "O")

    if field.check_win("X"):
        print("Крестики выиграли!")
    elif field.check_win("O"):
        print("Нолики выиграли!")
    else:
        print("Ничья.")


if __name__ == "__main__":
    tournament()

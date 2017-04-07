N = 67
T = 31


class Field:
    def __init__(self, width):
        self.width = width
        self.map = [0]*width

    def next_step(self):
        """рассчитать новое состояние поля"""
        next_map = [0]*self.width
        for i in range(1, self.width-1):
            next_map[i] = self.map[i-1] ^ self.map[i+1]
        self.map[:] = next_map

    def show(self):
        """ отобразить состояние поля """
        for x in self.map:
            print('*' if x else ' ', end='')
        print()

if __name__ == "__main__":
    field = Field(N)
    field.map[N//2] = 1
    field.show()
    for t in range(T):
        field.next_step()
        field.show()

def matryoshka(n):
    if n == 0:
        print('Крайняя матрёшечка!')
    else:
        print('  '*n + 'Верх матрёшки n =', n)
        matryoshka(n-1)
        print('  '*n + "Низ матрёшки n =", n)


def factorial(n):
    if n == 0:
        print("Крайний случай!")
        return 1
    else:
        print("Прямой ход рекурсии, n =", n)
        n1 = n - 1
        f1 = factorial(n1)  # Момент Х
        f = f1*n
        print("Обратный ход рекурсии, n =", n)
        return f

if __name__ == "__main__":
    matryoshka(5)
    f5 = factorial(5)
    print(f5)

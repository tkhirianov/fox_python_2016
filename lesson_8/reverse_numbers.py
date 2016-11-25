# вывести N чисел с клавиатуры в обратном порядке
n = int(input())
A = []
for i in range(n):
    x = int(input())
    A.append(x)

while len(A) > 0:
    x = A.pop()
    print(x)

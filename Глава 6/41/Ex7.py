'''Напишите программу, которая выполняет заливку одноцветной области заданным цветом.
Матрица, содержащая цвета пикселей, вводится из файла. Затем с клавиатуры
вводятся координаты точки заливки и цвет заливки. На экран нужно вывести
матрицу, которая получилась после заливки.'''

#просто пробовал
def printMatr(B):
    for i in range(len(B)):
        for j in range(len(B[i])):
            print ("{:4d}".format(B[i] [j]), end=" ")
        print()
B = [[0, 1, 0, 1, 1],
     [1, 1, 1, 2, 2],
     [0, 1, 0, 2, 2],
     [3, 3, 1, 2, 2],
     [0, 1, 1, 0, 0]]
#print(printMatr(A), "\n Сверху изначальная, снизу окрашенная")
'''yMax = len(B)
xMax = len(B[0])

new_color = 5
x0 = 2 #int(input("x"))
y0 = 1 #int(input("y"))
color = B[y0] [x0]

Q = [(x0, y0)]

while len(Q) > 0:
    x, y = Q.pop(0)
    if B[y] [x] == color:
        B[y] [x] = new_color'''
#print(printMatr(A))
"""Fin = open("Zalivka.txt")
A = []
lst = Fin.readlines()

for s in lst:
    print(s, end=" ")
    A += s
print("\nA =========\n", A)

yMax = len(A)
xMax = len(A[0])

new_color = 5
x0 = 2 #int(input("x"))
y0 = 1 #int(input("y"))
color = A[y0] [x0]

Q = [(x0, y0)]

while len(Q) > 0:
    x, y = Q.pop(0)
    if A[y] [x] == color:
        A[y] [x] = new_color
print(s)
Fin.close()"""

'''n = 5
matr = [[] for i in range(n)]
with open("Zalivka.txt") as file:
    for i in range(n):
        matr[i] = [t for t in file.readline().split()]

print(matr)'''
#Всё что выше можно удалить

Fin = open("Zalivka.txt")
matrix = [l.replace(" \n", "").split() for l in Fin]
print(matrix)

lst = Fin.readlines()

yMax = len(matrix)
xMax = len(matrix[0])

new_color = 5
print("Нумерация начинается с 0")
x0 = int(input("Номер столбца: "))
y0 = int(input("Номер строки: "))
color = matrix[y0] [x0]

Q = [(x0, y0)]

while len(Q) > 0:
    x, y = Q.pop(0)
    if matrix[y] [x] == color:
        matrix[y] [x] = new_color

print("Заменён цвет в ", y0+1,"й скобке, на ",x0 + 1, "й позиции", "\n", matrix, sep="")
Fin.close()



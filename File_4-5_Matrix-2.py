# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n \times mn×m и
# заполните её таблицей умножения по формуле mult[i][j] = i * j.

n, m = int(input()), int(input())
for i in range(n):
    mult = []
    for j in range(m):
        mult.append(str(i * j).ljust(3))
    print(*mult)


# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем n строк по m целых чисел в каждой, отделенных символом пробела.
#
# Напишите программу, которая находит индексы (строку и столбец)
# первого вхождения максимального элемента.

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j
print(row, col)


# Напишите программу, которая меняет местами столбцы в матрице.

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
x, y = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()


# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

n = int(input())
matrix = []
flag = 'YES'
for i in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 'NO'
print(flag)


# Дана квадратная матрица чисел.
# Напишите программу, которая меняет местами элементы,
# стоящие на главной и побочной диагонали,
# при этом каждый элемент должен остаться в том же столбце
# (то есть в каждом столбце нужно поменять местами элемент на
# главной диагонали и на побочной диагонали).

n = int(input())
matrix = []

for i in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)
for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()


# Дана квадратная матрица чисел.
# Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

n = int(input())
matrix = []

for i in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

for i in range(n // 2):
    matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
for row in matrix:
    print(*row)


# Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.

n = int(input())
matrix = []
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

for r in range(n):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()


# На шахматной доске 8×8 стоит конь. Напишите программу,
# которая отмечает положение коня на доске и все клетки,
# которые бьет конь. Клетку, где стоит конь,
# отметьте английской буквой N, клетки, которые бьет конь,
# отметьте символами *, остальные клетки заполните точками.

x,y = input()
n = 8
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97
matrix[y][x] = 'N'

for i in range(n):
    for q in range(n):
        if abs(i - y) * abs(q - x) == 2:
            matrix[i][q] = '*'

for x in range(n):
    print(*matrix[x])


# Магическим квадратом порядка n называется квадратная таблица размера n×n,
# составленная из всех чисел 1, 2, 3,…,n
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет,
# является ли заданная квадратная матрица магическим квадратом.

n = int(input())
matrix = []

for _ in range(n):
    temp = [int(x) for x in input().split()]
    matrix.append(temp)
digits = [i for i in range(1, n**2 +1)]

d1, d2 = 0, 0
for i in range(n):
    stolb_sum, stroka_sum = 0, 0
    for j in range(n):
        stolb_sum += matrix[j][i]
        stroka_sum += matrix[i][j]
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    d1 += matrix[i][i]
    d2 += matrix[i][n-i-1]
    if stolb_sum != stroka_sum:
        break
if stolb_sum == stroka_sum == d1 == d2 and digits == []:
    print('YES')
else:
    print('NO')


# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n \times mn×m и
# заполните её таблицей умножения по формуле mult[i][j] = i * j.

# n, m = int(input()), int(input())
# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i * j).ljust(3))
#     print(*mult)


# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем n строк по m целых чисел в каждой, отделенных символом пробела.
#
# Напишите программу, которая находит индексы (строку и столбец)
# первого вхождения максимального элемента.

# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
# print(row, col)


# Напишите программу, которая меняет местами столбцы в матрице.

# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# x, y = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
# for r in range(n):
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()


# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

# n = int(input())
# matrix = []
# flag = 'YES'
# for i in range(n):
#     temp = [int(i) for i in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             flag = 'NO'
# print(flag)


# Дана квадратная матрица чисел.
# Напишите программу, которая меняет местами элементы,
# стоящие на главной и побочной диагонали,
# при этом каждый элемент должен остаться в том же столбце
# (то есть в каждом столбце нужно поменять местами элемент на
# главной диагонали и на побочной диагонали).

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(i) for i in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for r in range(n):
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()


# Дана квадратная матрица чисел.
# Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(i) for i in input().split()]
#     matrix.append(temp)
#
# for i in range(n // 2):
#     matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
# for row in matrix:
#     print(*row)


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







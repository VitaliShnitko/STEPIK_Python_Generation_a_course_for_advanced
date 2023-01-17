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

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j
print(row, col)


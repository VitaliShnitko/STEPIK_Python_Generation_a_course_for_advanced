# На вход программе подаются два натуральных числа n и m,
# каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и т.д.
#
# Напишите программу, которая сначала считывает элементы матрицы один за другим,
# затем выводит их в виде матрицы.

# # 1 решение
#
# a = []
# n = int(input())    #stroka
# m = int(input())    #stolbec
#
# for i in range(n):
#     matrix = []
#     for i in range(m):
#         matrix.append(input())
#     a.append(matrix)
# for i in a:                         # вывод строк/столцов
#     print(*i)
#
# # 2 решение
# n = int(input())
# m = int(input())
#
# [print(*[input() for i in range(m)]) for i in range(n)]


# На вход программе подаются два натуральных числа n и m,
# каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и т.д.
#
# Напишите программу, которая считывает элементы матрицы один за другим,
# выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу,
# но уже поменяв местами строки со столбцами:
# первая строка выводится как первый столбец, и так далее.

# # 1 решение
# a = []
# n = int(input())    #stroka
# m = int(input())    #stolbec
#
# for i in range(n):
#     matrix = []
#     for i in range(m):
#         matrix.append(input())
#     a.append(matrix)
# for i in a:
#     print(*i)
#
# print()
#
# for c in range(m):                   # вывод столцов/строк
#     for r in range(n):
#         print(a[r][c], end=' ')
#     print()
#
#
# # 1 решение
# n, m = int(input()), int(input())
# w = [[input() for _ in range(m)] for _ in range(n)]
# [print(*r) for r in w]
# print()
# [print(*[w[j][i] for j in range(n)]) for i in range(m)]


# Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# s = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s += matrix[i][j]
# print(s)


# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     count = 0
#     s = 0
#     for j in range(n):
#         s += matrix[i][j]
#     for r in range(n):
#         if matrix[i][r] > s / n:
#             count += 1
#     print(count)


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# Нижнюю часть.

# n = int(input())
# matrix = []
# max_id = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             max_id.append(matrix[i][j])
# print(max(max_id))


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# n = int(input())
# matrix = []
# max_id = []
# for i in range(n):
#     temp = [int(i) for i in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j) and (i <= n - 1 - j):
#             max_id.append(matrix[i][j])
#         if (i <= j) and (i >= n - 1 - j):
#             max_id.append(matrix[i][j])
# print(max(max_id))


# Квадратная матрица разбивается на четыре четверти,
# ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов:
# верхней четверти; правой четверти; нижней четверти; левой четверти.

n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]

verh_ch = []
pr_ch = []
niz_ch = []
lv_ch = []

for i in range(n):
    for j in range(n):
        if (i < j) and (i < n - 1 - j):
            verh_ch.append(matrix[i][j])
        if (i < j) and (i > n - 1 - j):
            pr_ch.append(matrix[i][j])
        if (i > j) and (i > n - 1 - j):
            niz_ch.append(matrix[i][j])
        if (i > j) and (i < n - 1 - j):
            lv_ch.append(matrix[i][j])
print(f'''
Верхняя четверть: {sum(verh_ch)}
Правая четверть: {sum(pr_ch)}
Нижняя четверть: {sum(niz_ch)}
Левая четверть: {sum(lv_ch)}
      ''')

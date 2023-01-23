# '''
# На вход программе подаются два натуральных числа
# n и m. Напишите программу для создания матрицы размером
# n×m, заполнив её символами . и * в шахматном порядке.
#  В левом верхнем углу должна стоять точка.
#  Выведите полученную матрицу на экран, разделяя элементы пробелами.
# '''
#
# matrix = []
# n = input().split() # делаем список для ввода в одну строку
#
# for i in range(int(n[0])):
#     temp = []
#     for j in range(int(n[1])):
#         if (i + j) % 2 == 0:   # проверяем на четность и не четность
#             temp.append('.')
#         else:
#             temp.append('*')
#     matrix.append(temp)
#
# # выводим матрицу
# for i in matrix:
#     print(*i)


# '''
# На вход программе подается натуральное число n.
# Напишите программу, которая создает матрицу размером
# n×n и заполняет её по следующему правилу:
#
# -числа на побочной диагонали равны 1;
# -числа, стоящие выше этой диагонали, равны 0;
# -числа, стоящие ниже этой диагонали, равны 2.
#
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
# '''
#
# n = int(input())
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу
#
# for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][n-i-1] = 1
#     for j in range(n):
#         if i > n - 1 - j:
#             matrix[i][j] = 2
#
# for r in range(n):                     # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()


# '''
# На вход программе подаются два натуральных числа
# n и m. Напишите программу, которая создает матрицу размером
# n×m и заполняет её числами от
# 1 до n*m в соответствии с образцом.
# '''
#
# # 1 способ
#
# matrix = []
# x = input().split()
# n, m = int(x[0]), int(x[1])
#
# for _ in range(n):
#     temp = [i for i in range(m)]
#     matrix.append(temp)
#
#
# # заполнение числами
# count = 1
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = count
#         count += 1
#
# # вывод матрицы
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()
#
# # 2 способ
#
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# '''
# Заполнене 2
# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером
# n×m заполнив её в соответствии с образцом.
# '''
#
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i + j * n + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


'''
Заполнение 3
На вход программе подается натуральное число n.
 Напишите программу, которая создает матрицу размером
n×n заполнив её в соответствии с образцом.
'''

# n = int(input())
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу
#
# # заполняем главную и побочную диагонали единицами
# for i in range(n):
#     matrix[i][n-i-1] = 1
#     for j in range(n):
#         if i == j:
#             matrix[i][j] = 1
#
# # выводим матрицу
# for i in matrix:
#     print(*i)


'''
Заполнение 4
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером 
n×n заполнив её в соответствии с образцом.
'''

# создаем квадратную матрицу
n = int(input())
matrix = [[0]*n for _ in range(n)]

# заполняем единицами сначала оси, потом четверти
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1
    for j in range(n):
        if (i < j) and (i < n - 1 - j):
            matrix[i][j] = 1
        if (i > j) and (i > n - 1 - j):
            matrix[i][j] = 1
# выводим матрицу
for i in matrix:
    print(*i)







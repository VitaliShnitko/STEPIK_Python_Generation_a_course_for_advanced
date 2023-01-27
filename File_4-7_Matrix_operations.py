'''
Сложение матриц
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа
n и m — количество строк и столбцов в матрицах,
затем элементы первой матрицы, затем пустая строка,
 далее следуют элементы второй матрицы.
'''


n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(n)]

pustaya_stroka = input()

matrix_2 = [[int(i) for i in input().split()] for _ in range(n)]


mat_sum = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat_sum[i][j] = matrix[i][j] + matrix_2[i][j]

for i in mat_sum:
        print(*i)

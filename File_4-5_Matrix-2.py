# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n \times mn×m и
# заполните её таблицей умножения по формуле mult[i][j] = i * j.

n, m = int(input()), int(input())
for i in range(n):
    mult = []
    for j in range(m):
        mult.append(str(i * j).ljust(3))
    print(*mult)
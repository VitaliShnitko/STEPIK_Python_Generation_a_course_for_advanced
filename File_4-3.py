# На вход программе подается число nn. Напишите программу,
# которая создает и выводит построчно список,
# состоящий из nn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

# n = int(input())    # считываем значения n
#
# for i in range(n):
#     my_list = []
#     for j in range(1, n+1):
#         my_list.append(j)
#     print(my_list)
# print()


# На вход программе подается число nn. Напишите программу,
# которая создает и выводит построчно вложенный список,
# состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

# n = int(input())    # считываем значения n
# my_list = [list(range(1, i+1)) for i in range(1, n + 1)]
# for row in my_list:
#     print(row)


# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
# В этом треугольнике на вершине и по бокам стоят единицы.
# Каждое число равно сумме двух расположенных над ним чисел.

n = int(input())
lst = [[1]]
for i in range(1, n + 1):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
    lst.append(row)

print(lst[-1])


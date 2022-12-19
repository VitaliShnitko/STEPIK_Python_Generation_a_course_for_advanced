# На вход программе подаются два целых числа aa и bb. Напишите программу, которая выводит:
#
# сумму чисел a и b;
# разность чисел a и b;
# произведение чисел a и b;
# частное чисел a и b;
# целую часть от деления числа a на b;
# остаток от деления числа a на b;
# корень квадратный из суммы их 10-х степеней

def is_result(a, b):
    summa = a + b
    difference = a - b
    multi = a * b
    div = a / b
    division = a // b
    ost_division = a % b
    square_root = ((a ** 10) + (b ** 10)) ** 0.5

    print(summa, difference, multi, div, division, ost_division, square_root, sep='\n')

x, y = int(input()), int(input())

is_result(x, y)

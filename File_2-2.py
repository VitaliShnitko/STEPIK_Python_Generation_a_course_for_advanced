# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек,
# лежащих в каждой координатной четверти.


# number = int(input())
# first, second, third, fourth = 0, 0, 0, 0
#
# for _ in range(number):
#     x, y = map(int, input().split())
#     first += x > 0 and y > 0
#     second += x < 0 and y > 0
#     third += x < 0 and y < 0
#     fourth += x > 0 and y < 0
#
# print(f"Первая четверть: {first}")
# print(f"Вторая четверть: {second}")
# print(f"Третья четверть: {third}")
# print(f"Четвертая четверть: {fourth}")



# На вход программе подается строка текста из натуральных чисел.
# Из неё формируется список чисел. Напишите программу подсчета количества чисел,
# которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом.

num = [int(i) for i in input().split()]
count = 0

for i in range(1, len(num)):
    if int(num[i]) > int(num[i-1]):
        count += 1
print(count)





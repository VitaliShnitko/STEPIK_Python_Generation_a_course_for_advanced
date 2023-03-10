# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек,
# лежащих в каждой координатной четверти.


number = int(input())
first, second, third, fourth = 0, 0, 0, 0

for _ in range(number):
    x, y = map(int, input().split())
    first += x > 0 and y > 0
    second += x < 0 and y > 0
    third += x < 0 and y < 0
    fourth += x > 0 and y < 0

print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")



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


# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу, которая меняет местами
# соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов,
# то последний остается на своем месте.

num = input().split()
for i in range(0, len(num)-1, 2):
    num[i], num[i+1] = num[i+1], num[i]
print(*num)


# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу циклического сдвига элементов списка направо,
# когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

num = input().split()

num2 = num[-1:] + num[:-1]
print(*num2)


# На вход программе подается строка текста,
# содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел.
# Напишите программу для подсчета количества разных элементов в списке.

num = input().split()
count = 1
for i in range(0, len(num)-1):
    if num[i] != num[i+1]:
        count += 1
print(count)


# Напишите программу для определения, является ли число произведением двух чисел из данного набора,
# выводящую результат в виде ответа «ДА» или «НЕТ».
#
# Формат входных данных
# В первой строке подаётся число n (0 < n < 1000) – количество чисел в наборе.
# В последующих nn строках вводятся целые числа, составляющие набор (могут повторяться).
# Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

n = int(input())
a = [input() for i in range(n)]
pr = int(input())
count = 0

for i in range(len(a)):
    for j in range(len(a)):
        if int(a[i]) * int(a[j]) == pr and i != j:
            count += 1
        else:
            continue
if count > 0:
    print('ДА')
else:
    print('НЕТ')


# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу.
# Помогите ребятам бросить честный жребий и определить,
# кто будет делать очередной модуль нового курса.


# 1 решение
timur = input()
ruslan = input()

if ruslan == timur:
    print('ничья')
elif timur == 'камень' and ruslan == 'ножницы':
    print('Тимур')
elif timur == 'ножницы' and ruslan == 'бумага':
    print('Тимур')
elif timur == 'бумага' and ruslan == 'камень':
    print('Тимур')
else:
    print('Руслан')
#
# 2 решение
tm, rs = input(), input()
print('ничья' if tm == rs else 'Тимур' if tm + rs in 'каменьножницыбумагакамень' else 'Руслан')


# Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет,
# и решил усложнить игру. Теперь Тимур и Руслан играют в игру
# Камень, ножницы, бумага, ящерица, Спок.
# Помогите ребятам вновь бросить честный жребий и определить,
# кто будет делать следующий модуль в новом курсе.

tm, rs = input(), input()
print('ничья' if tm == rs else 'Тимур' if tm + rs in
'каменьножницыбумагакаменьящерицаСпокножницыящерицабумагаСпоккамень' else 'Руслан')


# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

text = input().split('О')
print(len(max(text)))


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными,
# состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

virus = 'anton'
for i in range(1, int(input()) + 1):
    s = input()
    res = ''
    for x in virus:
        if x in s:
            res += x
            s = s[s.find(x):]
    if res == virus:
        print(i, end=' ')


# Необходимо написать программу, реализующую алгоритм написания этой песни.
# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.


word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104) if chr(i) != 'ё']

for x in alpha:
    if x in word:
        print(word, x)
        word = word.replace(x, '').replace('  ', ' ').strip()








# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Вариант 1. Циклы тут тоже есть!!! XD
list_1 = [1, 2, 3, 4, 5]
print(list_1)
k = int(input('Введите число: '))
length = len(list_1) - k  # чтобы сделать новый список на то кол-во цифр, которое нужно перенести в хвост (5-3=2)
list_2 = []  # новый список будет в данном случае из двух символов
if len(list_1) < k or k <= 0:  # проверка, чтобы нормальное число вводили
    print(f'Число должно быть меньше либо равно {len(list_1)}')
else:
    for i in range(length):  # в новый список добавляем те цифры с хвоста первого списка, которые перейдут в начало
        list_2.append(list_1[k])
        k += 1
    concatenated_list = list_2 + list_1  # объединяем два списка в один, начиная с нового (хвостовые цифры)
    # print(concatenated_list)
    while len(concatenated_list) > len(list_1):  # отрезаем лишнее с хвоста нового длинного списка
        concatenated_list.pop(len(concatenated_list) - 1)  # в кол-ве лишних символов (в примере это 2 символа)
        # print(concatenated_list)  # проверка
    print(concatenated_list)

# Вариант 2 непонятный
list_1 = [1, 2, 3, 4, 5]
k = int(input('Введите число: '))
if len(list_1) < k or k <= 0:  # проверка, чтобы нормальное число вводили
    print(f'Число должно быть меньше либо равно {len(list_1)}')
else:
    temp = 0
    for i in range(len(list_1) - k):
        for j in range(len(list_1) - 1):
            temp = list_1[j]
            list_1[j] = list_1[j - 1]
            list_1[j - 1] = temp
    print(list_1)


# Вариант 3 как хотелось изначально, но не осилила сама
list_1 = [1, 2, 3, 4, 5]
k = int(input('Введите число: '))
for i in range(k):
    list_1.insert(0,list_1.pop())
print(list_1)

# Вариант 3
# list_1 = [1, 2, 3, 4, 5, 6]
# k = int(input('Введите число: '))
# length = len(list_1)
# print(list_1)
# if len(list_1) < k or k <= 0:  # проверка, чтобы нормальное число вводили
#     print(f'Число должно быть меньше либо равно {len(list_1)}')
# else:
#     for i in range(length):
#         list_1.remove(list_1[k])
#         list_1.insert(i, k)
#
# print(list_1)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 18, 19]
k = int(input('Введите число: '))
length = len(list_1) - k  # чтобы сделать новый список на то кол-во цифр, которое нужно перенести в хвост (5-3=2)
list_2 = []  # новый список будет в данном случае из двух символов
if len(list_1) < k or k <= 0:  # проверка, чтобы нормальное число вводили
    print(f'Число должно быть меньше либо равно {len(list_1)}')
else:
    for i in range(length):  # в новый список добавляем те цифры с хвоста первого списка, которые перейдут в начало
        list_2.append(list_1[k])
        k += 1
    # print(list_2)
    concatenated_list = list_2 + list_1  # объединяем два списка в один, начиная с нового (хвостовые цифры)
    print(concatenated_list)
    while len(concatenated_list) > len(list_1):  # отрезаем лишнее с хвоста нового длинного списка
        concatenated_list.pop(len(concatenated_list)-1)  # в кол-ве лишних символов (в примере это 2 символа)

    print(concatenated_list)

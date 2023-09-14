dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]  # список словарей
print(dictionaries)
unique_dictionary = set (val for dic in dictionaries for val in dic.values())
print(unique_dictionary)

dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]  # список словарей
print(dictionaries)
unique_dictionary = set (val for dic in dictionaries for val in dic.values())
print(unique_dictionary)


# 23
# Вариант 1 ручной ввод списка
list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list_1) - 1):
    if list_1[i] < list_1[i + 1]:
        count += 1

print(count, list_1)

# Вариант 2 рандомное заполнение списка

from random import randint

list_1 = []
for i in range(10):
    list_1.append(randint(-10, 11))
    count = 0
    for i in range(len(list_1) - 1):
        if list_1[i] < list_1[i + 1]:
            count += 1

print(count, list_1)

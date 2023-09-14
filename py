list_1 = [1, 2, 3, 4, 5]
k = int(input('Введите число: '))
length = len(list_1) - k
list_2 = []
if len(list_1) < k or k <= 0:
    print(f'Число должно быть меньше либо равно {len(list_1)}')
else:
    for i in range(length):
        list_2.append(list_1[k])
        k += 1
concatenated_list = list_2 + list_1
while len(concatenated_list) > len(list_1):
    concatenated_list.pop(concatenated_list[-1])

# print(list_1)
# print(list_2)
print(concatenated_list)

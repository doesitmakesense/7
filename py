n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
lst_1 = {int(input('Введите элемент первого множества: ')) for i in range(n)}
lst_2 = {int(input('Введите элемент второго множества: ')) for j in range(m)}

lst_3 = list(lst_1.intersection(lst_2))
lst_3.sort()
print(lst_3)

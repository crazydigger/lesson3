number = input('Пользователь вводит количество элементов будущего списка:')
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список#
l = []
for i in range(int(number)):
    new_item = input('введите число:')
    l.append(new_item)

    l = sorted(l)
    #l=l.sort()
    sorted(l, )

print(l)
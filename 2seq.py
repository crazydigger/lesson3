number = input('Пользователь вводит количество элементов будущего спискачерез запятую:')
# После этого по очереди по одной вводит любые цифрычерез запятую
separator = input('введите разделитель:[,;/')
if separator not in",;/":
    print("неверный разделитель!можно импользоватьзапятую точку с запятой и слэш")
# Сохранить цифры в список#

l = number.split(separator)
#список уникальных значений
l_uniq = set(l)
print(l)
print(l_uniq)
for i in range(int(number)):
    new_item = input('введите число:')
    l.append(new_item)

    l = sorted(l)
    #l=l.sort()
    sorted(l, )

print(l)
# Отсортировать список по возрастанию и вывести на экран
# Пример работы: Введите количество элементов: 3

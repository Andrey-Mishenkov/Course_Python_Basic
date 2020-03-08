#--------------------------------------------------------------------------------------------------------------------------------
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
print('\nЗадание 2\n')

list_change = []
stop_input = False
while (not stop_input):
    item = input('Введите элемент списка или "stop" для завершения ввода: ')
    if (item != 'stop'):
        list_change.append(item)
    else:
        stop_input = True

#list_change = ['ddd', '4545', 'True', 'jugv', 'False', '888', 'xxxzzz']
print('Исходный список =', list_change)

for i in range(1, len(list_change), 2):
    list_change[i - 1], list_change[i] = list_change[i], list_change[i-1]

print('Измененный список =', list_change)
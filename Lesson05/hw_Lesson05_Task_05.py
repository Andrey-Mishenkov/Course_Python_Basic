#--------------------------------------------------------------------------------------------------------------------------------
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

#----------------------------------------------------------------------------------------------------------------
# Функция создания файла
def create_file(count_numbers):
    """
    The creating of text file. A sequence of random numbers from 1 to 100, separated by spaces, is written to the file.
    :param count_numbers: int The quantity of numbers written to the file
    :return None
    """
    with open('Task_05.txt', 'w', encoding='utf-8') as file:
        for i in range(count_numbers):
            number = random.randint(0, 100)
            file.write(f'{number} ')

    print('Файл создан')

#----------------------------------------------------------------------------------------------------------------
# Основная программа
print('\nЗадание 5\n')

# Создаю файл из 10 случайных чисел
create_file(10)

# Читаю данные из файла; считаю общую сумму чисел
with open('Task_05.txt', 'r', encoding = 'utf-8') as file:

    total_sum = 0
    for line in file:

        print(f'Числа в файле: {line}')
        line = line.strip()                     # Удаляю служебные символы из строки файла
        list_numers = line.split(' ')           # Разделяю строку на отдельные числа

        while list_numers.count('') > 0:        # Удаляю пустые элементы из списка
            list_numers.remove('')

        for item in list_numers:
            if item.isdigit():
                total_sum += int(item)

print(f'Сумма чисел в файле = {total_sum}')
#--------------------------------------------------------------------------------------------------------------------------------
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# функция проверки на число
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# функция получения суммы
def fun_sum(str_number):
    result = 0

    # получаю список чисел (слов)
    list_numbers = str_number.split(' ')

    # удаляю лишние пробелы
    while '' in list_numbers:
        list_numbers.remove('')

    # перебор элементов списка: проверка на числа и накопление итоговой суммы
    for number in list_numbers:
        if is_digit(number):
            result += float(number)
        elif (number == '*'):         # найден символ окончания ввода
            break
        else:
            print ('Ошибка: введен недопустимый символ!')
            result = 0
            break

    return result

print('Задание 5')
stop_input = False
total_sum = 0
local_sum = 0

while not stop_input:
    str_numbers = input('Введите список чисел (через пробел) или символ * для окончания ввода: ')

    local_sum = fun_sum(str_numbers)
    total_sum += local_sum
    print(f'Локальная сумма чисел:   {local_sum}')
    print(f'Накопленная сумма чисел: {total_sum}')

    if ('*' in str_numbers):
        stop_input = True
        print('Вы ввели символ * - Выполнение завершено')
    else:
        print('Продолжаем...\n')


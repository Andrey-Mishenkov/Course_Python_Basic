#--------------------------------------------------------------------------------------------------------------------------------
#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def fun_div(a, b):
    result = None
    try:
        a = float(a)
        b = float(b)
        result = a / b
    except ZeroDivisionError:
        result = 'Ошибка: Деление на ноль!'
    except ValueError:
        result = f'Ошибка: Неверный тип аргументов: {a}, {b}'
    except TypeError:
        result = f'Ошибка: Неверные тип аргументов: {a}, {b}'

    return result

print('Задание 1')
stop_input = False
while not stop_input:

    a = input('Введите число - делимое:  ')
    b = input('Введите число - делитель: ')

    print(fun_div(a, b))

    is_stop = input('\nЗакончить ввод? Y/N: ')
    if (is_stop.upper() == 'Y'):
        stop_input = True
        print('Конец!')
    else:
        print('Продолжаем...\n')
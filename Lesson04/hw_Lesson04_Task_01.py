#--------------------------------------------------------------------------------------------------------------------------------
#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys

def calc_salary(work_hours, rate_hour, bonus):

    result = work_hours * rate_hour + bonus
    return result

print('Задание 1')

work_hours, rate_hour, bonus = 0, 0, 0

#  проверка параметра - Рабочие часы
try:
    work_hours = float(sys.argv[1])
except ValueError:
    print('Ошибка: параметр Рабочие часы - неверный тип данных')
except IndexError:
    print('Ошибка: не задан параметр Рабочие часы')
except Exception as e:
    print('Ошибка: параметр Рабочие часы - ', e)

#  проверка параметра - Ставка за час
try:
    rate_hour = float(sys.argv[2])
except ValueError:
    print('Ошибка: параметр Ставка за час - неверный тип данных')
except IndexError:
    print('Ошибка: не задан параметр Ставка за час')
except Exception as e:
    print('Ошибка: параметр Ставка за час - ', e)

#  проверка параметра - Премия
try:
    bonus = float(sys.argv[3])
except ValueError:
    print('Ошибка: параметр Премия - неверный тип данных')
except IndexError:
    print('Ошибка: не задан параметр Премия')
except Exception as e:
    print('Ошибка: параметр Премия - ', e)

total_sum = calc_salary(work_hours, rate_hour, bonus)

print(f'\nВы ввели:\n'
      f'\tРабочие часы  = {work_hours}\n'
      f'\tСтавка за час = {rate_hour}\n'
      f'\tПремия        = {bonus}\n'
      f'Итоговая заработная плата = {total_sum}')

#--------------------------------------------------------------------------------------------------------------------------------
# Пример ввода строки с параметрами для расчета
# D:\WORK\BI\GeekBrains\Course_Python_Basic\HomeWork_Clean>python Lesson04\hw_Lesson04_Task_01.py 160 750 25000

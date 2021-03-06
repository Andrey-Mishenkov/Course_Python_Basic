#--------------------------------------------------------------------------------------------------------------------------------
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print('\nЗадание 1\n')

my_var1 = 1000
my_var2 = 3.14159
my_var3 = 'Hello, world!'
my_var4 = True

print(f'my_var1 = {my_var1}\nmy_var2 = {my_var2}\nmy_var3 = {my_var3}\nmy_var4 = {my_var4}')

first_name  = input('\nВведите Имя: ')
second_name = input('Введите Фамилию: ')
age         = input('Введите возраст: ')

print(f'\nВы ввели:\n   Имя: {first_name}\n   Фамилия: {second_name}\n   Возраст: {age}')

#--------------------------------------------------------------------------------------------------------------------------------
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
print('\nЗадание 2\n')

time_sec = ''
while not time_sec.isdigit():
    time_sec = input('Введите время в секундах: ')

time_sec = int(time_sec)

hh = time_sec // 3600
mm = (time_sec - hh * 3600) // 60
ss = time_sec - hh * 3600 - mm * 60

print(f'В формате чч:мм:сс Вы ввели время: {hh:02}:{mm:02}:{ss:02}')

#--------------------------------------------------------------------------------------------------------------------------------
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('\nЗадание 3\n')

number = input('Введите число от 1 до 9: ')
while (not number.isdigit()) or (int(number) < 1) or (int(number) > 9):
    number = input('Введите число от 1 до 9: ')

number = int(number)
result = number + (number * 10 + number) + (number * 100 + number * 10 + number)
print(f'{number} + {number}{number} + {number}{number}{number} = {result}')

#--------------------------------------------------------------------------------------------------------------------------------
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print('\nЗадание 4\n')

number = input('Введите любое положительное целое число: ')
while (not number.isdigit()):
    number = input('Введите любое положительное целое число: ')

number = int(number)
number_max = 0
while (number > 0):
    div_mod = number % 10

    if (div_mod > number_max):
        number_max = div_mod

    number = number // 10

print(f'Максимальная цифра = {number_max}')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('\nЗадание 5\n')

revenue = ''
while (not revenue.isdigit()):
    revenue = input('Введите выручку фирмы: ')

cost = ''
while (not cost.isdigit()):
    cost = input('Введите затраты фирмы: ')

revenue = int(revenue)
cost    = int(cost)
fin_res = revenue - cost

if (fin_res > 0):
    print(f'Финансовый результат - прибыль: {fin_res} уе')
    print(f'Рентабельность деятельности: {round(fin_res / revenue, 2) * 100}%')
elif (fin_res < 0):
    print(f'Финансовый результат - убыток: {fin_res} уе')
else:
    print(f'Фирма отработала в ноль (выручка равна затратам:')

staff = ''
while (not staff.isdigit()):
    staff = input('Введите численность сотрудников фирмы: ')

staff = int(staff)
if (fin_res >= 0):
    print(f'Прибыль на одного сотрудника: {round(fin_res / staff, 2)} уе')
elif (fin_res < 0):
    print(f'Убыток на одного сотрудника: {round(fin_res / staff, 2)} уе')

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
print('\nЗадание 6\n')
i = 1
result = ''
while (not result.isdigit()):
    result = input('Введите результат спортсмена в 1-й день, км: ')

target = ''
while (not target.isdigit()):
    target = input('Введите цель спортсмена, км: ')

result = int(result)
target = int(target)

print(f'{i}-й день: {result}')
while (result < target):
    i += 1
    result = round(result * 1.1, 2)
    print(f'{i}-й день: {result}')

print(f'Ответ: на {i}-й день спортсмен достиг результата - не менее {target} км')

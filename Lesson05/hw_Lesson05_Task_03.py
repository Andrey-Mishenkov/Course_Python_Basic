#--------------------------------------------------------------------------------------------------------------------------------
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

print('\nЗадание 3\n')

with open('Task_03.txt', 'r', encoding = 'utf-8') as file:
    line_index = 0

    list_person = []            # Список сотрудников
    list_salary = []            # Список окладов
    list_salary_small = []      # Список признаков окладов меньше 20000
    # После чтения файла количество элементов в трех списках должно совпадать

    for line in file:
        line_index += 1

        line = line.strip()                     # Удаляю служебные символы из строки файла
        list_word = line.split(' ')             # Разделяю строку на слова

        while list_word.count('') > 0:          # Удаляю пустые элементы из списка
            list_word.remove('')

        # Разбор
        if (len(list_word) > 0):
            # print(list_word)

            # оклад и признак низкого оклада
            salary, is_small_salary = 0, 0
            if len(list_word) > 1 and list_word[1].isdigit():
                salary = int(list_word[1])

                if (salary < 20000):
                    is_small_salary = 1

            # Добавление очередных элементов в списки
            list_person.append(list_word[0])            # Сотрудник
            list_salary.append(salary)                  # Оклад
            list_salary_small.append(is_small_salary)   # Признак низкого оклада

# Вывод данных
print('Список сотрудников =', list_person)
print('Список окладов =', list_salary)
print('Список низких окладов =', list_salary_small)

print('\nНизкие оклады:')
for i in range(len(list_salary_small)):
    list_small_salary = []

    if list_salary_small[i] == 1:
        print(f'\t{list_person[i]}; {list_salary[i]}')

# Расчет среднего оклада
salary_avg = 0
if len(list_salary):
    salary_avg = round( sum(list_salary) / len(list_salary) )

print(f'Средний оклад по всем сотрудникам = {salary_avg}')

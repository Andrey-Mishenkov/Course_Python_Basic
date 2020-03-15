#--------------------------------------------------------------------------------------------------------------------------------
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def in_func(word):

    list_letter = 'abcdefghijklmnopqrstuvwxyz '
    result = None
    is_error = False

    for letter in word:
        if (not letter in list_letter):
            print('Ошибка ввода: Недопустимый символ(ы)')
            is_error = True
            break

    if (not is_error):
        result = word.title()

    return result

print('Задание 6')
stop_input = False

while not stop_input:

    word = input('Введите влово (маленькими латинскими буквами): ')
    print(in_func(word))

    is_stop = input('\nЗакончить ввод? Y/N: ')

    if (is_stop.upper() == 'Y'):
        stop_input = True
        print('Конец!')
    else:
        print('Продолжаем...\n')

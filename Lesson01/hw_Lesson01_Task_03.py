#--------------------------------------------------------------------------------------------------------------------------------
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('\nЗадание 3\n')

number = input('Введите число от 1 до 9: ')
while (not number.isdigit()) or (int(number) < 1) or (int(number) > 9):
    number = input('Введите число от 1 до 9: ')

number = int(number)
result = number + (number * 10 + number) + (number * 100 + number * 10 + number)
print(f'{number} + {number}{number} + {number}{number}{number} = {result}')


#--------------------------------------------------------------------------------------------------------------------------------
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('\nЗадание 3\n')

number = ''
while (not number.isdigit()) or (int(number) < 1):
    number = input('Введите положительное число: ')

result = 0
i = 1
while i <= 3:
    result += int(number * i)
    i += 1

print(f'{number} + {number}{number} + {number}{number}{number} = {result}')
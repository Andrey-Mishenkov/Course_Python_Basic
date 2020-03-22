#--------------------------------------------------------------------------------------------------------------------------------
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

#--------------------------------------------------------------------------------------------------------------------------------
class Worker:
    name:     str = ''
    surname:  str = ''
    position: str = ''
    _income = {
                'wage': 0,
                'bonus': 0
                }

    # --------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, name, surname, position, wage, bonus):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
        self._income['wage'] = wage
        self._income['bonus'] = bonus

#--------------------------------------------------------------------------------------------------------------------------------
class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

#--------------------------------------------------------------------------------------------------------------------------------
# Основная программа
print('\nЗадание 3')

person_1 = Position('Иван',  'Иванов',  'Директор',  150000, 70000)
person_2 = Position('Петр',  'Петров',  'Грузчик',   25000,  15000)
person_3 = Position('Семен', 'Семенов', 'Бухгалтер', 60000,  0)

print('\nИмена:')
print('\t', person_1.name,     person_2.name,     person_3.name)

print('\nФамилии:')
print('\t', person_1.surname,  person_2.surname,  person_3.surname)

print('\nДолжности:')
print('\t', person_1.position, person_2.position, person_3.position)

print('\nПолные имена:')
print('\t', person_1.get_full_name())
print('\t', person_2.get_full_name())
print('\t', person_3.get_full_name())

print('\nОбщий доход:')
print('\t', person_1.get_total_income())
print('\t', person_2.get_total_income())
print('\t', person_3.get_total_income())
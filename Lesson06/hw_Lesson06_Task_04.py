#--------------------------------------------------------------------------------------------------------------------------------
# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

#--------------------------------------------------------------------------------------------------------------------------------
class Car:
    name:  str = ''
    color: str = ''
    is_police: bool = False
    speed: int = 0

    def __init__(self, name, color, is_police, speed):

        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print('\tПоехала')

    def stop(self):
        print('\tОстановилась')

    def turn(self, direction):
        print(f'\tПовернула {direction}')

    def show_speed(self):
        return self.speed

#--------------------------------------------------------------------------------------------------------------------------------
class TownCar(Car):

    def show_speed(self):
        alarm_high_speed = ''
        if (self.speed > 60):
            alarm_high_speed = ' - High speed! (town car)'

        return f'{self.speed}{alarm_high_speed}'

#--------------------------------------------------------------------------------------------------------------------------------
class SportCar(Car):

    def show_speed(self):
        return self.speed

#--------------------------------------------------------------------------------------------------------------------------------
class WorkCar(Car):

    def show_speed(self):
        alarm_high_speed = ''
        if (self.speed > 40):
            alarm_high_speed = ' - High speed! (work car)'

        return f'{self.speed}{alarm_high_speed}'

#--------------------------------------------------------------------------------------------------------------------------------
class PoliceCar(Car):

    def show_speed(self):
        return self.speed

#--------------------------------------------------------------------------------------------------------------------------------
# Основная программа
print('\nЗадание 4')

car_1 = TownCar('Ford',         'blue',       False, 50)
car_2 = TownCar('Scoda',        'white',      False, 70)
car_3 = SportCar('Ferrari',     'red',        False, 70)
car_4 = WorkCar('Volkswagen',   'orange',     False, 45)
car_5 = PoliceCar('Toyota',     'white-blue', True, 70)

print('\nМарки машин:')
print('\t', car_1.name, car_2.name, car_3.name, car_4.name, car_5.name)

print('\nЦвета:')
print('\t', car_1.color, car_2.color, car_3.color, car_4.color, car_5.color)

print('\nПринадлежность полиции:')
print('\t', car_1.is_police, car_2.is_police, car_3.is_police, car_4.is_police, car_5.is_police)

print('\nТекущая скорость:')
print(f'\t{car_1.name}\t{car_1.show_speed()}')
print(f'\t{car_2.name}\t{car_2.show_speed()}')
print(f'\t{car_3.name}\t{car_3.show_speed()}')
print(f'\t{car_4.name}\t{car_4.show_speed()}')
print(f'\t{car_5.name}\t{car_5.show_speed()}')

print('\nДвижение:')
print(f'Это машина {car_1.name}')
car_1.go()
car_1.turn('налево')
car_1.go()
car_1.turn('направо')
car_1.stop()

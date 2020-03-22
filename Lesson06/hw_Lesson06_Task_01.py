#--------------------------------------------------------------------------------------------------------------------------------
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight:
    __color: str = 'красный'     #

    # продолжительность включения, секунды
    __time_red:     int = 7     # красный свет
    __time_yellow:  int = 2     # желтый свет
    __time_green:   int = 5     # зеленый свет
    __font_color = '\033[31m'

    # --------------------------------------------------------------------------------------------------------------------------------
    # переключение режимов работы
    def running(self, second = 0):

        if  self.__color == 'красный' and second > self.__time_red:
            TrafficLight.__color = 'желтый'
            self.__font_color = '\033[33m'

        elif self.__color == 'желтый' and second > self.__time_yellow:
            TrafficLight.__color = 'зеленый'
            self.__font_color = '\033[32m'

        elif self.__color == 'зеленый' and second > self.__time_green:
            TrafficLight.__color = 'красный'
            self.__font_color = '\033[31m'

        return TrafficLight.__color

    def get_font_color(self):
        return self.__font_color

#--------------------------------------------------------------------------------------------------------------------------------
# Основная программа
print('\nЗадание 1\n')

total_time = ''
while not total_time.isdigit():
    total_time = input('Задайте общее время работы светофора в секундах (много не надо, 30-60 секунд достаточно): ')
total_time = int(total_time)

tl = TrafficLight()                     # объект класса TrafficLight
second = 0
color_current = tl.running(second)      # начальный состояние объекта

for i in range(total_time):

    time.sleep(1)
    second += 1
    color_prev = color_current
    color_current = tl.running(second)

    # текущее состояние светофора
    if color_current != color_prev:
        print(f'\033[30m---> Переключение! {tl.get_font_color()}({color_prev} >> {color_current})' if color_current != color_prev else '')
        second = 0
    else:
        print(f'\033[30m({i+1} из {total_time}) : {tl.get_font_color()}{second} сек - {color_current}')

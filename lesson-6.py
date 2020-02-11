# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при
# его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(2)
            i += 1


TrafficLight = TrafficLight() # Помешаем наш класс в переменную
TrafficLight.running() # Метод обекто-потока,выводим нашу программу

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, _length, _winth):
        self._length = _length
        self._winth = _winth

    def mass(self):
        ret =  self._length * self._winth * 25 * 5 / 1000
        print(f'{ret}')


road = Road(20, 5000)
road.mass()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Possition(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + '-' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


user = Possition('Marat', 'Popov', 'Designer', 50000, 8000)
print(f' Name: {user.get_full_name()} \n Position: {user.position} \n Salary: {user.get_total_income()}')

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Cars:

    def __init__(self, name, speed, color, is_police = 40):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return 'Вперед -'

    def stop(self):
        return 'Стоп'

    def turn_left(self):
        return 'Поворот на лево -'

    def turn_rigth(self):
        return 'Поворот на право -'

class TownCar(Cars):

    def __init__(self, name, speed, color, family = 60):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, 90)

bmw = TownCar('BMW', 60, 'Black')
porshe = SportCar('Porshe', 180, 'Yellow')
audi = WorkCar('Audi', 90, 'Grey', 60)
ford = PoliceCar('Ford', 180, 'red')
print(bmw.name, bmw.color, bmw.speed, bmw.is_police)
print(bmw.go(), bmw.turn_left(), bmw.turn_rigth(), bmw.stop())
print(porshe.name, porshe.color, porshe.speed, porshe.is_police)
print(porshe.go(), porshe.turn_rigth(), porshe.stop())
print(audi.name, audi.color, audi.speed, audi.is_police)
print(audi.go(), audi.turn_left(), audi.stop())
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn_left(), ford.stop())







































"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

"""Наверное с практической стороны более правильный вариант, но делая крайнее задание заметил, что тут написано 
как и там, что классы дочерние, в конце, в комментарии прикрепил решение с дочерними классами"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return 'Полицейская машина поехала.'
        else:
            return 'Машина поехала.'

    def stop(self):
        return 'Машина остановлена.'

    def turn(self, direction):
        return f' Машина едет на{direction}.'

    def show_speed(self):
        if self.name == 'TownCar':
            if self.speed > 60:
                return f'Превышение максимально разрешенной скорости, сбросьте скорость на {self.speed - 60}км/ч.'
        elif self.name == 'WorkCar':
            if self.speed > 40:
                return f'Превышение максимально разрешенной скорости, сбросьте скорость на {self.speed - 40}км/ч.'
        else:
            return f'Скорость автомобиля {self.speed}км/ч.'


car1 = Car(82, 'хром', 'TownCar')
print(car1.go(), car1.show_speed(), car1.turn('лево'), car1.turn('право'), car1.stop(), 'Конец поездки')
car2 = Car(98, 'черный', 'WorkCar')
print(car2.go(), car2.turn('лево'), car2.show_speed(), car2.turn('право'), car2.stop(), 'Конец поездки')
car3 = Car(325, 'красный', 'SportCar')
print(car3.go(), car3.show_speed(), car3.turn('право'), car3.stop(), 'Конец поездки, спасибо )))')
car4 = Car(110, 'серый', 'PoliceCar', True)
print(car4.go(), car4.show_speed(), car4.stop(), 'Конец поездки.')

"""
Второй вариант:

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала.'

    def stop(self):
        return 'Машина остановлена.'

    def turn(self, direction):
        return f' Машина едет на{direction}.'

    def show_speed(self):
        return f'Скорость автомобиля {self.speed}км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение максимально разрешенной скорости, сбросьте скорость на {self.speed - 60}км/ч.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение максимально разрешенной скорости, сбросьте скорость на {self.speed - 40}км/ч.'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def go(self):
        if self.is_police:
            return 'Полицейская машина поехала.'


car1 = TownCar(82, 'хром', 'TownCar')
print(car1.go(), car1.show_speed(), car1.turn('лево'), car1.turn('право'), car1.stop(), 'Конец поездки')
car2 = WorkCar(98, 'черный', 'WorkCar')
print(car2.go(), car2.turn('лево'), car2.show_speed(), car2.turn('право'), car2.stop(), 'Конец поездки')
car3 = SportCar(325, 'красный', 'SportCar')
print(car3.go(), car3.show_speed(), car3.turn('право'), car3.stop(), 'Конец поездки, спасибо )))')
car4 = PoliceCar(110, 'серый', 'PoliceCar', True)
print(car4.go(), car4.show_speed(), car4.stop(), 'Конец поездки.')
"""

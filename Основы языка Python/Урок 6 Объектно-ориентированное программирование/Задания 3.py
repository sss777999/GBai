"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        m = self._income['wage'] + (self._income['wage'] * self._income['bonus'])
        return int(m)


i = Position('Ivan', 'Ivanov', 'ceo', {'wage': 100, 'bonus': 0.1})
i1 = i.get_total_income()
print(f'{i.get_full_name()} have {i1}$ hour profit')
m = Position('Mihail', 'Prohorov', 'managing partner', {'wage': 1500, 'bonus': 0.25})
m1 = m.get_total_income()
print(f'{m.get_full_name()} have {m1}$ hour profit')
v = Position('V', 'B', 'owner', {'wage': 77777, 'bonus': 0.75})
v1 = v.get_total_income()
print(f'{v.get_full_name()} have {v1}$ hour profit')

"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def m(cls, date):
        return cls([int(i) for i in date if i[0][0] != 0])

    @staticmethod
    def v(date):
        return date[0] <= 31 and date[1] <= 12 and date[2] > 0


inp = input('Enter date with spaces: ')
d = Data(inp.split())
c = d.m(inp.split())
print(f'DD {c.date[0]} MM {c.date[1]} YY {c.date[2]}')
print(f'Validating of date is: {d.v(c.date)}')

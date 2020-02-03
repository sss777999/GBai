"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Check(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


try:
    imp = int(input('Enter one integer: '))
    if imp == 0:
        raise ValueError
    imp1 = int(input('Enter 0: '))
    if imp1 == 0:
        raise Check('Wrong')
except ValueError:
    print('Wrong integer')
except Check as err:
    print(err)

"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

winhrs, phrs, prize = int(argv[1]), int(argv[2]), int(argv[3])


def payment(w, ph, p):
    return (w * ph) + p


print(f'Your salary calculations: {payment(winhrs, phrs, prize)}')

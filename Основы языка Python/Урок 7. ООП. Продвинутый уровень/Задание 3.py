"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления
должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        celladd = self.num + other.num
        return celladd

    def __sub__(self, other):
        cellsub = self.num - other.num
        if cellsub > 0:
            return cellsub
        else:
            return f'Разность должна быть больше 0, в данном случае {cellsub}'

    def __mul__(self, other):
        cellmul = self.num * other.num
        return cellmul

    def __truediv__(self, other):
        celltdiv = round(self.num // other.num)  # зачем round, если целочисленное деление?
        return celltdiv

    def make_order(self, n):
        s = ''
        count = self.num
        laststr = self.num % n
        if laststr != 0:
            while count > n:
                for j in range(n):
                    s += '*'
                count -= n
                s += '\n'
            s += ('*' * laststr)
        else:
            while count > 0:
                for j in range(n):
                    s += '*'
                count -= n
                s += '\n'
        return s


c1 = Cell(27)
c2 = Cell(2)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
c3 = Cell.make_order(c1, 5)
print(c3)

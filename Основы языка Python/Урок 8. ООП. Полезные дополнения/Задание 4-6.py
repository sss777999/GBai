"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
"""

"""Можно еще очень много чего создавать и фантазировать )))"""
d = {}


class Warehouse:
    def __init__(self, d):
        self.d = d

    def pr(self=None):
        return d


class Equipment:
    def __init__(self, n, dep, q):
        self.n = n
        self.dep = dep
        try:                                                # при вводе строки завершает программу с принтом
            self.q = int(q)
        except ValueError:
            print('Wrong integer. Run program again')
            exit()

    def income(self):
        if len(d) == 0:
            d[self.dep] = [[self.n, self.q]]
        else:
            for i in d.keys():
                if self.dep not in d.keys():
                    d[self.dep] = [[self.n, self.q]]
                    break
                else:
                    d[self.dep].append([self.n, self.q])
                    break

    @staticmethod
    def move(fdep, fn, tdep):
        lst = []
        for m in d[tdep]:
            lst.append(m[0])
        for i in d[fdep]:
            if i[0] == fn:
                for j in d[tdep]:
                    if j[0] == fn:
                        j[1] += i[1]
                        d[fdep].remove(i)
                        break
            if fn not in lst:
                d[tdep].append(i)
                d[fdep].remove(i)
                break


class Printer(Equipment):
    def __init__(self, model):
        self.model = model

    def get_pr(self):
        for i in d:
            for j in d[i]:
                if j[0] == 'printer':
                    return f'In "{i}" we have {j[1]} printers, model - "{self.model}"'


class Xerox(Equipment):
    def __init__(self, model):
        self.model = model

    def get_xr(self):
        for i in d:
            for j in d[i]:
                if j[0] == 'xerox':
                    return f'In "{i}" we have {j[1]} xeroxes, model - "{self.model}"'


class Scanner(Equipment):
    def __init__(self, model):
        self.model = model

    def get_sc(self):
        for i in d:
            for j in d[i]:
                if j[0] == 'scanner':
                    return f'In "{i}" we have {j[1]} scanners, model - "{self.model}"'


# создаем департаменты с оргтехникой
s = Equipment('scanner', 'General', 29)
s.income()
x = Equipment('xerox', 'General', 15)
x.income()
p = Equipment('printer', 'Store', 55)
p.income()
xx = Equipment('xerox', 'Store', 15)
xx.income()
print(f'Before other actions we had in warehouse: {d}')

# перемещаем между департаментами
Equipment.move('General', 'scanner', 'Store')
Equipment.move('Store', 'printer', 'General')
Equipment.move('General', 'xerox', 'Store')
print(f'After moving some equipment we have: {Warehouse.pr()}')

# в личных классах храним в каком департаменте, в каком количестве и какой модели оборудование есть
pr = Printer('Canon')
print(pr.get_pr())
xr = Xerox('Anon')
print(xr.get_xr())
sc = Scanner('Non')
print(sc.get_sc())

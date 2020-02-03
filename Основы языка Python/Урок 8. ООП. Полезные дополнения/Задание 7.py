"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

a = '2+i'
b = '3+4i'


class Complexint:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):

        for i in range(len(self.n)):
            for j in range(len(other.n)):
                self.n[i] = self.n[i] + other.n[j]
                i += 1
            break
        return Complexint(self.n)

    def __mul__(self, other):
        for i in range(len(self.n)):
            for j in range(len(other.n)):
                try:
                    self.n[i] = (self.n[i] * other.n[j] - self.n[i + 1] * other.n[j + 1])
                    self.n[i + 1] = (self.n[i] * other.n[j + 1] + self.n[i + 1] * other.n[j])
                except IndexError:
                    pass
            break
        return Complexint(self.n)

    def __str__(self):
        final = [str(i) for i in self.n]
        final = '+'.join(final)
        return f'{final}i'


a = a[:-1].split(',')
b = b[:-1].split(',')

for i in a:
    minuscount = i.count('-')
    if '+' in i:
        i = i.split('+')
        if i[1] == '':
            i[1] = '1'
    if '-' in i:
        i = i.split('-')
        if i[1] == '':
            i[1] = '1'
        if minuscount == 1:
            i[-1] = f'-{i[-1]}'
        if minuscount == 2:
            i[-1] = f'-{i[-1]}'
            i[-2] = f'-{i[-2]}'
            i.remove('')
    a = i
    a = [int(i) for i in a]

# print(a)

for j in b:
    minuscount = j.count('-')
    if '+' in j:
        j = j.split('+')
        if j[1] == '':
            j[1] = '1'
    if '-' in j:
        j = j.split('-')
        if j[1] == '':
            j[1] = '1'
        if minuscount == 1:
            j[-1] = f'-{j[-1]}'
        if minuscount == 2:
            j[-1] = f'-{j[-1]}'
            j[-2] = f'-{j[-2]}'
            j.remove('')
    b = j
    try:
        b = [int(m) for m in b]
    except ValueError:
        pass
#print(b)

x = Complexint(a)
y = Complexint(b)

#print(x + y)
print(x * y)  # тестировать или + или *, не одновременно

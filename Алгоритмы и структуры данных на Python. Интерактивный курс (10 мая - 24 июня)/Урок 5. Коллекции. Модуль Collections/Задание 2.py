'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в
данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
'''
import collections

d = collections.defaultdict()
count = 10
letters = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(letters)):
    d[letters[i]] = count
    count += 1

char = input('Введите + для сложения, * для произведения: ')
n1 = input('Введите первое шестнадцатиричное число: ').split()
n2 = input('Введите второе шестнадцатиричное число: ').split()
c = []
''' для быстрой проверки
char = '*'
n1 = ['C', 4, 'F']
n2 = ['A', 2]
'''


# переводим в десятичные
def num10(numlist):
    res = 0
    l = len(numlist) - 1
    for i in numlist:
        if i in d.keys():
            i = d[i]
            res += i * pow(16, l)
        else:
            res += int(i) * pow(16, l)
        l -= 1
    return res


# переводим в шестнадцатиричные
def num16(n):
    while n >= 15:
        m = n % 16
        n = n // 16
        for k, v in d.items():
            if v == m:
                m = k
        c.append(m)
    if n in d.values():
        for k, v in d.items():
            if v == n:
                n = k
                c.append(n)
    else:
        c.append(n)

    c.reverse()
    return c


# print(num10(n1))  # первое число в 10
# print(num10(n2))  # второе число в 10
first = num10(n1)
second = num10(n2)
if char == '*':
    result = first * second
else:
    result = first + second

# print(result)  # получившееся число
print(num16(result))

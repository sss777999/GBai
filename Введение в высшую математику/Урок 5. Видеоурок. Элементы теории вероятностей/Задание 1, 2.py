"""Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро)."""
import random
import matplotlib.pyplot as plt
import numpy as np

print('Задача 1')
for i in range(10):
    # print(f'Крутим рулекту {i+1} раз')
    a = random.randint(0, 36)
    if 0 < a <= 18:
        print(f'Число на черном поле {a}')
    elif a > 18:
        print(f'Число на красном поле {a}')
    if a == 0:
        print(f'Зеро {a}')
print()
"""Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере 
рулетки или подбрасывания монетки.
Сгенерируйте десять выборок случайных чисел х0, …, х9.
и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.
"""

print('Задача 2.1')
m = 1  # нужный исход
n = 2  # возможных вариантов
n1 = 2  # количество бросков
o = n ** n1  # возможные виды выпадений
pr = m / n  # шанс выпадения орла
po = m / n  # шанс выпадения орла
p = (pr + po) / o  # шанс выпадения 2 орлов одновременно при подбрасывании двух монет одновременно
print(f'Вероятность {p} или {round(p * 100)}%')

resh = 0
orel = 0
# при броске из 4 раз в большинстве случаев выходит 0.25
for i in range(4):
    g = random.randint(1,2)
    g1 = random.randint(1,2)
    if g == 1 and g1 == 1:
        resh += 1
print(resh/4)

print('Задача 2.1')
lst = []
for i in range(10):
    rand = np.random.rand(10)
    lst.append(rand)
num_bins = 5
n, bins, patches = plt.hist(sum(lst), num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
# если я правильно понял условие



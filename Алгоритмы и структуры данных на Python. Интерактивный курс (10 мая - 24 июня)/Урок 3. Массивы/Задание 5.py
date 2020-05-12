'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

a = [random.randint(-5, 5) for i in range(random.randint(5, 10))]
print(a)
maxmin = 0
min = 0
place = 'Отсутствует'
for i in range(len(a)):
    if a[i] < 0 and maxmin == 0:
        maxmin = a[i]
        place = i
    if a[i] < 0:
        min = a[i]
    if a[i] < 0 and maxmin < a[i]:
        maxmin = a[i]
        place = i
if maxmin == 0:
    print('Нет такого отрицательного числа')
else:
    print(f'Максимальный отрицательный элемент: {maxmin}, индекс: {place}')

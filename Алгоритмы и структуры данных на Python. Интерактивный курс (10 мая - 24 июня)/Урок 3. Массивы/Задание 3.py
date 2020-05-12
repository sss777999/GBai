'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

a = [random.randint(0, 100) for i in range(random.randint(0, 50))]
max = 0
min = a[0]
placemin = None
placemax = None
print(a)
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
    if min > a[i]:
        min = a[i]

for i in range(len(a)):
    if a[i] == min:
        placemin = i
    elif a[i] == max:
        placemax = i
mi = a[placemin]
ma = a[placemax]
print(
    f'Индекс минимального числа: {placemin} число {a[placemin]}\nИндекс максимального числа: {placemax} число {a[placemax]}')
a.pop(placemin)
a.insert(placemin, ma)
a.pop(placemax)
a.insert(placemax, mi)
print(a)

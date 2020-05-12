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
print(f'Индекс минимального числа: {placemin}\nИндекс максимального числа: {placemax}')

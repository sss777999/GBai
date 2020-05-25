'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

import random

a = [random.randint(-100, 100) for i in range(20)]
print(a)


def swap(arr, left_pos, right_pos):
    temp = arr[left_pos]
    arr[left_pos] = arr[right_pos]
    arr[right_pos] = temp


def bubble_sort(arr):
    for itm in arr:
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)


bubble_sort(a)
a.reverse()
print(a)

'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой
переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.
'''
import random
import sys

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
print('*' * 50)
print(sys.version, sys.platform)
print('*' * 50)


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


s = [a, max, min, placemin, placemax, mi, ma]
for i in s:
    print(i)
    show_size(i)
    print('*' * 50)

'''
**************************************************
3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] darwin
**************************************************
[63, 23, 1, 39, 20, 85, 22, 15, 72, 98, 23, 19, 35, 29, 97, 25, 18, 90, 63, 46, 29, 23, 33, 90, 23, 58, 5, 53, 21, 12, 72, 45, 21, 80, 16, 67, 3, 6, 79, 25, 8, 61, 41]
 type=<class 'list'>, size= 424, object= [63, 23, 1, 39, 20, 85, 22, 15, 72, 98, 23, 19, 35, 29, 97, 25, 18, 90, 63, 46, 29, 23, 33, 90, 23, 58, 5, 53, 21, 12, 72, 45, 21, 80, 16, 67, 3, 6, 79, 25, 8, 61, 41]
	 type=<class 'int'>, size= 28, object= 63
	 type=<class 'int'>, size= 28, object= 23
	 type=<class 'int'>, size= 28, object= 1
	 type=<class 'int'>, size= 28, object= 39
	 type=<class 'int'>, size= 28, object= 20
	 type=<class 'int'>, size= 28, object= 85
	 type=<class 'int'>, size= 28, object= 22
	 type=<class 'int'>, size= 28, object= 15
	 type=<class 'int'>, size= 28, object= 72
	 type=<class 'int'>, size= 28, object= 98
	 type=<class 'int'>, size= 28, object= 23
	 type=<class 'int'>, size= 28, object= 19
	 type=<class 'int'>, size= 28, object= 35
	 type=<class 'int'>, size= 28, object= 29
	 type=<class 'int'>, size= 28, object= 97
	 type=<class 'int'>, size= 28, object= 25
	 type=<class 'int'>, size= 28, object= 18
	 type=<class 'int'>, size= 28, object= 90
	 type=<class 'int'>, size= 28, object= 63
	 type=<class 'int'>, size= 28, object= 46
	 type=<class 'int'>, size= 28, object= 29
	 type=<class 'int'>, size= 28, object= 23
	 type=<class 'int'>, size= 28, object= 33
	 type=<class 'int'>, size= 28, object= 90
	 type=<class 'int'>, size= 28, object= 23
	 type=<class 'int'>, size= 28, object= 58
	 type=<class 'int'>, size= 28, object= 5
	 type=<class 'int'>, size= 28, object= 53
	 type=<class 'int'>, size= 28, object= 21
	 type=<class 'int'>, size= 28, object= 12
	 type=<class 'int'>, size= 28, object= 72
	 type=<class 'int'>, size= 28, object= 45
	 type=<class 'int'>, size= 28, object= 21
	 type=<class 'int'>, size= 28, object= 80
	 type=<class 'int'>, size= 28, object= 16
	 type=<class 'int'>, size= 28, object= 67
	 type=<class 'int'>, size= 28, object= 3
	 type=<class 'int'>, size= 28, object= 6
	 type=<class 'int'>, size= 28, object= 79
	 type=<class 'int'>, size= 28, object= 25
	 type=<class 'int'>, size= 28, object= 8
	 type=<class 'int'>, size= 28, object= 61
	 type=<class 'int'>, size= 28, object= 41
**************************************************
98
 type=<class 'int'>, size= 28, object= 98
**************************************************
1
 type=<class 'int'>, size= 28, object= 1
**************************************************
9
 type=<class 'int'>, size= 28, object= 9
**************************************************
2
 type=<class 'int'>, size= 28, object= 2
**************************************************
1
 type=<class 'int'>, size= 28, object= 1
**************************************************
98
 type=<class 'int'>, size= 28, object= 98
**************************************************
'''

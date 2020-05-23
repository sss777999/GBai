'''3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.'''

import random
import sys

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {r}')

max = r[0]
min = r[0]

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив осле изменения элементов {min_index} и {max_index}: {r}')

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


s = [r, max, min, min_index, max_index]
for i in s:
    print(i)
    show_size(i)
    print('*' * 50)

'''
**************************************************
3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] darwin
**************************************************
[9, 2, 23, 66, 18, 28, 88, 30, 77, 73]
 type=<class 'list'>, size= 184, object= [9, 2, 23, 66, 18, 28, 88, 30, 77, 73]
	 type=<class 'int'>, size= 28, object= 9
	 type=<class 'int'>, size= 28, object= 2
	 type=<class 'int'>, size= 28, object= 23
	 type=<class 'int'>, size= 28, object= 66
	 type=<class 'int'>, size= 28, object= 18
	 type=<class 'int'>, size= 28, object= 28
	 type=<class 'int'>, size= 28, object= 88
	 type=<class 'int'>, size= 28, object= 30
	 type=<class 'int'>, size= 28, object= 77
	 type=<class 'int'>, size= 28, object= 73
**************************************************
88
 type=<class 'int'>, size= 28, object= 88
**************************************************
2
 type=<class 'int'>, size= 28, object= 2
**************************************************
6
 type=<class 'int'>, size= 28, object= 6
**************************************************
1
 type=<class 'int'>, size= 28, object= 1
**************************************************
'''

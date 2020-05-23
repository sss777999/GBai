'''3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.'''

# самый лучший вариант, т.к. использует меньше всего памяти. В учет не берем что a random.
import random
import sys

a = [random.randint(0, 100) for i in range(random.randint(0, 50))]
max = a.index(max(a))
min = a.index(min(a))

a[max], a[min] = a[min], a[max]

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


s = [a, max, min]
for i in s:
    print(i)
    show_size(i)
    print('*' * 50)

'''
**************************************************
3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] darwin
**************************************************
[15, 48, 34, 13, 41, 62, 61, 57, 63, 20, 29, 55, 37, 73, 69, 93, 42, 64, 35, 1, 44, 49, 63, 100, 43, 96, 78]
 type=<class 'list'>, size= 336, object= [15, 48, 34, 13, 41, 62, 61, 57, 63, 20, 29, 55, 37, 73, 69, 93, 42, 64, 35, 1, 44, 49, 63, 100, 43, 96, 78]
	 type=<class 'int'>, size= 28, object= 15
	 type=<class 'int'>, size= 28, object= 48
	 type=<class 'int'>, size= 28, object= 34
	 type=<class 'int'>, size= 28, object= 13
	 type=<class 'int'>, size= 28, object= 41
	 type=<class 'int'>, size= 28, object= 62
	 type=<class 'int'>, size= 28, object= 61
	 type=<class 'int'>, size= 28, object= 57
	 type=<class 'int'>, size= 28, object= 63
	 type=<class 'int'>, size= 28, object= 20
	 type=<class 'int'>, size= 28, object= 29
	 type=<class 'int'>, size= 28, object= 55
	 type=<class 'int'>, size= 28, object= 37
	 type=<class 'int'>, size= 28, object= 73
	 type=<class 'int'>, size= 28, object= 69
	 type=<class 'int'>, size= 28, object= 93
	 type=<class 'int'>, size= 28, object= 42
	 type=<class 'int'>, size= 28, object= 64
	 type=<class 'int'>, size= 28, object= 35
	 type=<class 'int'>, size= 28, object= 1
	 type=<class 'int'>, size= 28, object= 44
	 type=<class 'int'>, size= 28, object= 49
	 type=<class 'int'>, size= 28, object= 63
	 type=<class 'int'>, size= 28, object= 100
	 type=<class 'int'>, size= 28, object= 43
	 type=<class 'int'>, size= 28, object= 96
	 type=<class 'int'>, size= 28, object= 78
**************************************************
19
 type=<class 'int'>, size= 28, object= 19
**************************************************
23
 type=<class 'int'>, size= 28, object= 23
**************************************************
'''

"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('integers.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7')

with open('integers.txt', 'r') as s:
    a = s.read().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print(f'Sum of integers: {sum(a)}')

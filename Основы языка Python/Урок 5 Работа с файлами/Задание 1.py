"""Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('file.txt', 'w', encoding='utf8') as f:
    a = 's'
    while a:
        a = input('Enter some data or press "Enter" for exit: ')
        f.write(a + '\n')

# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка
# можно не запрашивать у пользователя, а указать явно, в программе.


l = ['a', 9, ['1', '2'], (4, '7'), {'a': 1}, 8.9]
for _ in l:
    print(type(_))

"""
4. Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты перестановок
для других значений n и k
"""

import itertools

count = 0
for p in itertools.permutations('0123456', 7):
    ''.join(str(x) for x in p)
    count += 1
print(f'Количество строк: {count}')

count = 0
for p in itertools.combinations('01234567', 4):
    ''.join(p)
    count += 1
print(f'Количество строк: {count}')

count = 0
for p in itertools.product("01", repeat=7):
    ''.join(p)
    count += 1
print(f'Количество строк: {count}')

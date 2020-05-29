'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

n = int(input('Введите количество друзей: '))  # количество друзей
count = 0
is_passed = []
g = [[1 for i in range(n)] for j in range(n)]
for i in range(len(g)):
    for j in range(len(g)):
        if j == 0 and count == 0:
            g[i][j] = 0
            count += 1
            i += 1
        if j == count:
            g[i][j] = 0
            count += 1
            i += 1
print(f'Смежный граф')
for i in g:
    print(i)
print('*' * 25)
# num = len(g) * (len(g) - 1) быстрый вариант
for i in g:
    for j in i:
        if j == 1:
            is_passed.append(True)
# print(is_passed)
num = is_passed.count(True)
print(f'Количество рукопожатий: {num}\nКоличество друзей: {n}')

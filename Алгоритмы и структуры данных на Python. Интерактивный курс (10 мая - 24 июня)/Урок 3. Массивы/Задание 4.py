'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random

a = [random.randint(0, 5) for i in range(random.randint(0, 20))]
print(a)
count = 0
count1 = 1
max = 0

for i in a:
    count1 = 0
    for j in a:
        if i == j:
            count1 += 1
    if count1 > count:
        max = i
        count = count1
print(f'Максимальное количество раз в массиве повторяется число: {max}')

'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
count1 = 0
count2 = 0
a = input('Введите число: ')
for i in a:
    if int(i)%2==0:
        count1+=1
    else:
        count2+=1

print(f'Четных: {count1}, нечетных {count2}')

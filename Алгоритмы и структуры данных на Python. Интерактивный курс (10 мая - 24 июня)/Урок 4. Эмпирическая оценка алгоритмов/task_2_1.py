'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
# >>> sieve(2)
3
# >>> prime(4)
7
# >>> sieve(5)
11
# >>> prime(1)
2
'''
import cProfile

# с решетом Эратосфена
# алгоритм показал лучший результат, сложность O(N**2)

n = 2000 # номер простого числа
mul = 10  # множитель


def sieve(n, mul):
    sieve = [i for i in range(n * mul)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n * mul:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[n - 1]


# print(sieve(n, mul)) # само число

# cProfile.run('sieve(n,mul)')
# 6 function calls in 0.013 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#         1    0.009    0.009    0.012    0.012 task_2_1.py:26(sieve)
#         1    0.002    0.002    0.002    0.002 task_2_1.py:27(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_2_1.py:36(<listcomp>)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# python3 -m timeit -n 100 -s "import task_2_1" "task_2_1.sieve(2000, 10)"
# 100 loops, best of 5: 5.14 msec per loop

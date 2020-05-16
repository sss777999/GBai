'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.
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
import timeit
import cProfile


# с помощью итератора


def main():
    n = 2000  # номер простого числа

    def primes():
        a = 2
        while True:
            k = 0
            for j in range(2, a):
                if a == 2:
                    continue
                if a % j == 0:
                    k += 1
            if k == 0:
                yield a
            else:
                k = 0
            a += 1

    prime = primes()
    for i in range(n):
        primenumber = next(prime)
    # print(primenumber)  # само число


# cProfile.run('main()')
# 4006 function calls in 11.778 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   11.778   11.778 <string>:1(<module>)
#         1    0.003    0.003   11.778   11.778 task_2_2.py:24(main)
#      2001   11.772    0.006   11.772    0.006 task_2_2.py:26(primes)
#         1    0.000    0.000   11.778   11.778 {built-in method builtins.exec}
#      2000    0.004    0.000   11.775    0.006 {built-in method builtins.next}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#  python3 -m timeit -n 3 -s "import task_2_2" "task_2_2.main()"
# 3 loops, best of 5: 10.9 sec per loop


# 2 вариант с timeit.timeit
'''
mycode = \'''
n = 2000


def primes():
    a = 2
    while True:
        k = 0
        for j in range(2, a):
            if a == 2:
                continue
            if a % j == 0:
                k += 1
        if k == 0:
            yield a
        else:
            k = 0
        a += 1


prime = primes()
for i in range(n):
    primenumber = next(prime)
# print(primenumber)

print(f'Выполнился за {timeit.timeit(stmt=mycode, number=1)} секунд.')
# Выполнился за 11.061634963 секунд.
'''

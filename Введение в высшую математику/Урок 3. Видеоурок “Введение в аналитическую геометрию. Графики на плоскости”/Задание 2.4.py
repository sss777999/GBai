"""
4. Задание (в программе)
Решите систему уравнений:
y = x2 – 1
exp(x) + x∙(1 – y) = 1


Решите систему уравнений и неравенств:
y = x2 – 1
exp(x) + x∙(1 – y) > 1
"""
import numpy as np
from scipy.optimize import fsolve


# 1
def equations(p):
    x, y = p
    return y - x ** 2 - 1, np.exp(x) + x * (1 - y) - 1


x1, y1 = fsolve(equations, (1, 1))
print(x1, y1)


#2
def equations(p):
    x, y = p
    return y - x ** 2 - 1, np.exp(x) + x * (1 - y) > 1


x1, y1 = fsolve(equations, (1, 1))
print(x1, y1)
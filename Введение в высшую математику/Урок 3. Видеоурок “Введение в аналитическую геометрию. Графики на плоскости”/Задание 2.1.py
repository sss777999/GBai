"""
1. Задание (в программе)
Нарисуйте график функции:
y(x) = k∙cos(x – a) + b
для некоторых (2-3 различных) значений параметров k, a, b
"""

import numpy as np
import matplotlib.pyplot as plt

k, a, b = 1, 2, 3
k1, a1, b1 = 2, 3, 4
k2, a2, b2 = 4, 3, 1
x = np.linspace(-2*np.pi, 3*np.pi, 201)
plt.plot(x, k * np.cos(x-a)+b)
plt.plot(x, k1 * np.cos(x-a1)+b1)
plt.plot(x, k2 * np.cos(x-a2)+b2)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
"""
5. Задание (в программе)
Нарисуйте трехмерный график двух параллельных плоскостей.
Нарисуйте трехмерный график двух любых поверхностей второго порядка.
"""

# 1
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 2)
Y = np.arange(-10, 10, 4)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)
Z2 = 2 * X - 3 * Y
ax.plot_surface(X, Y, Z2)
ax.plot_surface(X, Y, Z - 400)
show()

# 2
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)
Z2 = np.sqrt(X ** 2 + Y ** 2)
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, -Z2)
ax.scatter(0, 0, 0, 'z', 50, 'red')
show()

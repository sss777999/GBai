"""
3. Задание (в программе)
Напишите код на Python, реализующий построение графиков:
окружности,
эллипса,
гиперболы.
"""
# Не совсем понял, что тут должно быть вообще. Matplotlib кроме пары моментов не изучали, значит наверное
# формулы, но переведенные в Python

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-3,3,41)
X,Y=np.meshgrid(t,t)
plt.figure()
plt.contour(X, Y, X**2-Y**2-1, [0], linewidths=3,colors='b')
plt.contour(X, Y, X**2/9+Y**2/4-1, [0], linewidths=3,colors='r')
plt.contour(X, Y, X**2 + Y**2, [1],linewidths=3,colors='y')
plt.gcf().set_facecolor('w');
plt.gcf().gca().axis('image');
plt.gcf().gca().grid(True)
plt.show()

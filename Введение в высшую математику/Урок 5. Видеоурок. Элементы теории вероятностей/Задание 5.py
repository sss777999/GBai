"""
5. Дополните код расчетом коэффициента корреляции x и y по формуле
"""
import matplotlib.pyplot as plt
import numpy as np

n = 100
r = 0.7
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
b = (np.sum(y) - a * np.sum(x)) / n
# коэфициент корреляции
r = (np.sum(x - (x + y / 2) * (y - (x + y / 2)))) / (
    np.sqrt(np.sum((x - (x + y / 2)) ** 2) * np.sum((y - (x + y / 2)) ** 2)))
# ---------------------
A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])
plt.show()

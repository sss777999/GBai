import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.cos(x)
z = np.cos(x+ 0.5)
plt.plot(x, y)
plt.plot(x, z)
print(x)
plt.show()
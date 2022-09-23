import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 100, 100000)
y = np.exp(-x*np.sin(x))
plt.ylabel("Это ось Y")
plt.xlabel("Это ось X")
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.minorticks_on()
plt.plot(x, y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 100, 10)
y = x**(-2)*np.sin(x)
plt.ylabel("Это ось Y")
plt.xlabel("Это ось X")
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.plot(x, y)
plt.show()
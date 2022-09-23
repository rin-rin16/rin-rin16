import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 100, 100000)
y = np.exp(-x*np.sin(x))
plt.plot(x, y)
plt.show()
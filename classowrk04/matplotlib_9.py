import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 100, 100000)
y = np.exp(x*np.sin(x))
plt.ylabel("Это ось Y в логарифмическом масштабе")
plt.xlabel("Это ось X")
plt.title("Красивый график")
plt.yscale('log')
plt.plot(x, y, "k--", label = "Чёрные точки")
plt.legend()
plt.show()
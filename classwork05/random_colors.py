import numpy as np
import matplotlib
from matplotlib import pyplot as plt

np.random.seed(5)
a = np.random.normal(0, 20, 30000).reshape(100, 100, 3)
plt.matshow(a)
plt.show()

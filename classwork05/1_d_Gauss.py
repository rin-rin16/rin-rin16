import numpy as np
import matplotlib
from matplotlib import pyplot as plt

np.random.seed(5)
a = np.random.normal(0, 2, 1000)
plt.hist(a, 'auto', label = 'Gauss')
plt.show()
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

np.random.seed(10000)
x = np.random.poisson(100, 10000)
np.random.seed(1000)
y = np.random.poisson(100, 10000)
xed = np.linspace(60, 140, 80)
yed = np.linspace(60, 140, 80)

distrib, xed, yed = np.histogram2d(x, y, bins = (xed, yed))

fig, axs = plt.subplots(1, 1)

axs.matshow(distrib)
axs.set_xticklabels([50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
axs.set_yticklabels([50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
plt.show()
import numpy as np

array = np.linspace(0, 35, 36).reshape(6, 6)

print(array, "\n")
print(array.sum(axis=1), "\n")
print(array.mean(axis=0), "\n")
import numpy as np
vector = np.array([i for i in range(1, 100)])
vec3 = np.array([vector[i] for i in range(0, len(vector), 3)])
print(vec3)
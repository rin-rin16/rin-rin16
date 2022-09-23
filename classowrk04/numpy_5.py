import numpy as np
vector = np.array([i for i in range(1, 100)])
vec3sum = np.array([])
for j in range(0, len(vector), 3):
    summm = sum(vector[i] for i in range (j, j+3))
    helpfull = np.array([summm])
    vec3sum = np.concatenate((vec3sum, helpfull))
vecshape = np.reshape(vec3sum, (11, 3))
vectransp = vecshape.T
print(vectransp)
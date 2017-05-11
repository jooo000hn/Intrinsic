import matplotlib.pyplot as plt
import numpy as np

exp = 2.0
near = 1.0
far = 10000.0
volumeDepth = 128.0

def volumeZToDepth(depth):
    return np.power(depth, exp) * far + near

t1 = np.arange(0.0, 1.0, 0.1)

plt.plot(t1, volumeZToDepth(t1), 'bo', t1, volumeZToDepth(t1), 'k')
plt.ylabel('Depth')
plt.xlabel('Volume Z')
plt.show()

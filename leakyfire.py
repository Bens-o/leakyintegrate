import numpy as np
import matplotlib.pyplot as plt
import math as math


t = np.arange(0,0.2,0.01)
c = 1000
r = 0.00002
tau = c * r
It = 0.1
vr = -70
vm = np.zeros(np.size(t))

for i in range(np.size(t)):
    vm[i] = vr + math.exp((-t[i] - t[0])/tau)


print(vm)

plt.plot(t, vm)
plt.show()

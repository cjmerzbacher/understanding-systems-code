import numpy as np
import math
from matplotlib import pyplot as plt

# Constants
r = 0.5 # intrinsic growth rate
K = 800 # carrying capacity
h = 50
A = 30

# Saturation Demo
def saturation(n):
    return h*n/(A+n)

pops = np.linspace(0., K)

fig = plt.figure()
ax = plt.axes(ylim=(0,5*h/4))
plt.plot(pops, saturation(pops))
plt.plot(pops, [h]*50, 'r--', label='h')
plt.legend()

ax.grid()
ax.invert_xaxis()
plt.xlabel("Stock")
plt.ylabel("Yield")

plt.show()
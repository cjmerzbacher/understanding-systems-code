import numpy as np
from math import exp
from matplotlib import pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Sliders
growth = widgets.FloatSlider(min=0.1, max=0.8)
carrying = widgets.IntSlider(min=10., max = 1000.)
initial = widgets.IntSlider(min=5., max = 1200.)
print("Growth rate: ")
display(growth)
print("Carrying Capacity: ")
display(carrying)
print("Initial population: ")
display(initial)

# Constants
r = growth.value  # growth rate
K = carrying.value  # carrying capacity
n_zero = initial.value  # population at t=0
A = (K-n_zero)/n_zero

# Plot logistic time series

def logistic(times):
    n = []
    for t in times:
        n.append(K/(1+A*exp(-r*t)))
    return n

t = np.linspace(0., 40)

plt.plot(t, logistic(t))
plt.plot(t, [K]*50, 'r--', label='K')
plt.legend()
plt.xlabel('time, day')
plt.ylabel('Fish Stock')

plt.show()